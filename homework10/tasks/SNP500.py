import asyncio
import json
from decimal import ROUND_HALF_UP, Decimal
from operator import itemgetter

import aiohttp
from bs4 import BeautifulSoup


class Round(Decimal):
    """Round values up to .00 using Decimal lib"""

    def __init__(self):
        super().__init__()

    def f(self, value):
        """Method to round values up to .00 using Decimal lib and convert it to float.
        :rtype: float
        """
        self.value = value
        fl_val = Decimal(self.value).quantize(Decimal("1.00"), ROUND_HALF_UP)
        floating_point = float(fl_val)
        return floating_point


async def get_response(url):
    """Function to get html code"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            return html


async def get_company_link(html):
    """Function to get company link (common table)"""
    soup = BeautifulSoup(html, "lxml")
    table = soup.find_all("td", class_="table__td table__td--big")
    list_of_links = []
    for link in table:
        part = link.find("a").get("href")
        list_of_links.append("https://markets.businessinsider.com" + part)
    return list_of_links


async def get_company_growth(html):
    """Function to get company year growth (common table)"""
    rounder = Round()
    soup = BeautifulSoup(html, "lxml")
    table = soup.find_all("tr")[1:]
    list_of_growth = []
    for growth in table:
        gr = growth.find_all("span")[9].get_text().rstrip("%")
        list_of_growth.append({"growth, %": rounder.f(gr)})
    return list_of_growth


async def get_exchange_rate():
    """Function to get RUB/USD exchange rate"""
    rate = await get_response("https://www.cbr.ru/scripts/XML_daily.asp?")
    rounder = Round()
    soup = BeautifulSoup(rate, "lxml")
    RUB_USD_rate = soup.find(text="Доллар США").next.text
    value = RUB_USD_rate.replace(",", ".")
    float_rate = rounder.f(value)
    return float_rate


async def content_from_company_page(html, exchange_rate):
    """Function to get company code, name, price, P/E and potential_profit from company page"""

    company_info = []
    rounder = Round()
    soup = BeautifulSoup(html, "lxml")

    code = (
        soup.find("span", class_="price-section__category")
        .find("span")
        .text.lstrip(", ")
    )
    name = soup.find("span", class_="price-section__label").text.strip()
    price = rounder.f(
        soup.find("span", class_="price-section__current-value").text.replace(",", "")
    )
    price_in_rub = rounder.f(price * exchange_rate)

    try:
        price_to_earnings = rounder.f(
            soup.find(text="P/E Ratio", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        price_to_earnings = 0

    try:
        week_high_52 = rounder.f(
            soup.find(text="52 Week High", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        week_high_52 = 0
    try:
        week_low_52 = rounder.f(
            soup.find(text="52 Week Low", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        week_low_52 = 0

    try:
        max_potential_profit = rounder.f(
            ((week_high_52 - week_low_52) / week_low_52) * 100
        )
    except ZeroDivisionError:
        max_potential_profit = 0

    company_info.append(
        {
            "code": code,
            "name": name,
            "price, RUB": price_in_rub,
            "growth, %": None,
            "price_to_earnings, r.u.": price_to_earnings,
            "52 Week High, USD": week_high_52,
            "52 Week Low, USD": week_low_52,
            "max potential profit per year, %": f"{max_potential_profit}",
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
    task_to_get_exchange_rate = asyncio.create_task(get_exchange_rate())
    exchange_rate = await task_to_get_exchange_rate
    growth_list = []
    total_info = []

    task_to_get_common_pages = [
        asyncio.create_task(get_response(url)) for url in url_list
    ]
    pages = await asyncio.gather(*task_to_get_common_pages)

    task_to_get_links_for_each_company = [
        asyncio.create_task(get_company_link(page)) for page in pages
    ]
    task_to_get_growth_for_each_company = [
        asyncio.create_task(get_company_growth(page)) for page in pages
    ]
    link_list = await asyncio.gather(*task_to_get_links_for_each_company)

    growth = await asyncio.gather(*task_to_get_growth_for_each_company)
    for lst in growth:
        for element in lst:
            growth_list.append(element)

    for collected_links in link_list:
        task_to_collect_htmls = [
            asyncio.create_task(get_response(url)) for url in collected_links
        ]
        collect_htmls = await asyncio.gather(*task_to_collect_htmls)
        companies_info = [
            asyncio.create_task(content_from_company_page(html, exchange_rate))
            for html in collect_htmls
        ]
        collected_info = await asyncio.gather(*companies_info)
        for lst in collected_info:
            for element in lst:
                total_info.append(element)

    return unite_growth_and_other_info(growth_list, total_info)


def sorting_dicts(data, condition):
    """Function to get top 10 companies according to given conditions"""
    if condition == "price_to_earnings, r.u.":
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
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = asyncio.run(main(url_list))

    for condition in [
        "price, RUB",
        "price_to_earnings, r.u.",
        "growth, %",
        "max potential profit per year, %",
    ]:
        with open(condition.split(", ")[0] + ".json", "w") as file:
            json.dump(sorting_dicts(data, condition), file)
