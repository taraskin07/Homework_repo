import asyncio
import json
from decimal import ROUND_HALF_UP, Decimal
from operator import itemgetter

import aiohttp
from bs4 import BeautifulSoup


class Round(Decimal):
    """Round values up to .00 using Decimal lib"""

    def __init__(self, value):
        self = float(self.quantize(Decimal("1.00"), ROUND_HALF_UP))


async def get_response(url):
    """Function to get html code"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


#
# class Company:
#     def __init__(self, link):
#         self.link = link


async def get_company_link(html):
    """Function to get company link (common table)"""
    soup = BeautifulSoup(html, "lxml")
    table = soup.find_all("td", class_="table__td table__td--big")
    list_of_links = []
    for link in table:
        part = link.find("a").get("href")
        list_of_links.append({"link": "https://markets.businessinsider.com" + part})
    return list_of_links


async def get_company_growth(html):
    """Function to get company year growth (common table)"""
    soup = BeautifulSoup(html, "lxml")
    table = soup.find_all("tr")[1:]
    list_of_growth = []
    for growth in table:
        gr = growth.find_all("span")[9].get_text().rstrip("%")
        list_of_growth.append({"growth, %": Round(gr)})
    return list_of_growth


async def get_exchange_rate():
    """Function to get RUB/USD exchange rate"""
    rate = await get_response("https://www.cbr.ru/scripts/XML_daily.asp?")
    soup = BeautifulSoup(rate, "lxml")
    RUB_USD_rate = soup.find(text="Доллар США").next.text
    float_rate = Round(RUB_USD_rate.replace(",", "."))
    return float_rate


async def content_from_company_page(html, exchange_rate):
    """Function to get company code, name, price, P/E and potential_profit from company page"""
    company_info = []
    soup = BeautifulSoup(html, "lxml")

    code = (
        soup.find("span", class_="price-section__category")
        .find("span")
        .text.lstrip(", ")
    )
    name = soup.find("span", class_="price-section__label").text.strip()
    price = Round(
        soup.find("span", class_="price-section__current-value").text.replace(",", "")
    )
    price_in_rub = price * exchange_rate
    price_to_earnings = Round(
        soup.find(text="P/E Ratio", class_="snapshot__header").previous_sibling.strip()
    )
    week_high_52 = Decimal(
        soup.find(
            text="52 Week High", class_="snapshot__header"
        ).previous_sibling.strip()
    )
    week_low_52 = Decimal(
        soup.find(
            text="52 Week Low", class_="snapshot__header"
        ).previous_sibling.strip()
    )
    max_potential_profit = float((week_high_52 - week_low_52) / week_low_52) * 100
    company_info.append(
        {
            "code": code,
            "name": name,
            "price, RUB": Round(price_in_rub),
            "growth, %": None,
            "P/E, r.u.": price_to_earnings,
            "52 Week High, USD": Round(week_high_52),
            "52 Week Low, USD": Round(week_low_52),
            "Max potential profit per year, %": f"{Round(max_potential_profit)}",
        }
    )

    return company_info


def unite_growth_and_other_info(list_of_growth, company_info):
    """Function to include growth data in final list"""
    growth_info = iter(list_of_growth)
    for el in company_info:
        el["growth, %"] = next(growth_info)["growth, %"]
    return company_info


async def main(url_list):
    """Function to get html pages asynchronously"""
    exchange_rate = asyncio.create_task(get_exchange_rate())

    pages = [asyncio.create_task(get_response(url)) for url in url_list]
    await asyncio.gather(*pages)

    link_list = [asyncio.create_task(get_company_link(page)) for page in pages]
    growth_list = [asyncio.create_task(get_company_growth(page)) for page in pages]
    await asyncio.gather(*link_list)
    await asyncio.gather(*growth_list)

    collect_htmls = [
        asyncio.create_task(get_response(url)) for url in [i["link"] for i in link_list]
    ]
    await asyncio.gather(*collect_htmls)

    companies_info = [
        asyncio.create_task(content_from_company_page(html, exchange_rate))
        for html in collect_htmls
    ]

    return unite_growth_and_other_info(growth_list, companies_info)


def sorting_dicts(data, condition):
    """Function to get top 10 companies according to given conditions"""
    if condition == "P/E, r.u.":
        data.sort(key=itemgetter(condition))
    else:
        data.sort(key=itemgetter(condition), reverse=True)
    top10 = []
    generated_list_of_companies = data[:10]
    for company in generated_list_of_companies:
        top10.append(
            {
                "code": company["code"],
                "name": company["name"],
                str(condition): company[condition],
            }
        )
    return top10


if __name__ == "__main__":
    url_list = [
        "https://markets.businessinsider.com/index/components/s&p_500?p=" + str(i)
        for i in range(1, 11)
    ]
    exchange_rate = get_exchange_rate()
    data = asyncio.run(main(url_list))
    for condition in [
        "price, RUB",
        "P/E, r.u.",
        "growth, %",
        "Max potential profit per year, %",
    ]:
        with open(condition + ".json", "w+") as file:
            json.dump(sorting_dicts(data, condition), file)


# loop = asyncio.get_event_loop()
# abc = loop.run_until_complete(get_response('https://markets.businessinsider.com/index/components/s&p_500?p=1'))
# # print(abc)
# # print(get_company_link(abc))
# # print(get_company_growth(abc))
# # print(get_exchange_rate())
# mmm = loop.run_until_complete(get_response('https://markets.businessinsider.com/stocks/mmm-stock'))
# exchange_rate = await get_exchange_rate()
# gr = get_company_growth(abc)
# common = content_from_company_page(mmm, exchange_rate)
# print(common)
#
# print(unite_growth_and_other_info(gr, common))
