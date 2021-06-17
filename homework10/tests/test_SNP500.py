import asyncio

import homework10.tasks.SNP500 as snp

Round = snp.Round
content_from_company_page = snp.content_from_company_page
get_company_growth = snp.get_company_growth
get_company_link = snp.get_company_link
get_response = snp.get_response
sorting_dicts = snp.sorting_dicts
unite_growth_and_other_info = snp.unite_growth_and_other_info


def test_Round():
    rounder = Round()
    test_value_float = 54.75567
    test_value_str = "54.75567"
    assert rounder.f(test_value_float) == 54.76
    assert rounder.f(test_value_str) == 54.76


def test_get_company_link():

    html = asyncio.run(
        get_response("https://markets.businessinsider.com/index/components/s&p_500?p=1")
    )
    list_of_links = asyncio.run(get_company_link(html))
    assert list_of_links[0] == "https://markets.businessinsider.com/stocks/mmm-stock"


def test_get_company_growth():
    html = asyncio.run(
        get_response("https://markets.businessinsider.com/index/components/s&p_500?p=1")
    )
    list_of_growth = asyncio.run(get_company_growth(html))
    assert list_of_growth[0]["growth, %"] == 27.68


def test_content_from_company_page():
    html = asyncio.run(
        get_response("https://markets.businessinsider.com/stocks/mmm-stock")
    )
    company_info = asyncio.run(content_from_company_page(html, 1))
    assert company_info[0]["code"] == "MMM"


def test_unite_growth_and_other_info():
    list2 = [
        {
            "code": "company code",
            "name": "company name",
            "price, RUB": "price_in_rub",
            "growth, %": None,
            "price_to_earnings, r.u.": "P/E",
            "52 Week High, USD": "week_high_52",
            "52 Week Low, USD": "week_low_52",
            "max potential profit per year, %": "max_potential_profit",
        }
    ]
    list1 = [
        {
            "growth, %": 90,
        }
    ]

    assert unite_growth_and_other_info(list1, list2)[0]["growth, %"] == 90


def test_main():
    pass


def test_sorting_dicts():
    data = [
        {
            "code": "company code1",
            "name": "company name1",
            "price, RUB": 1,
        },
        {
            "code": "company code4",
            "name": "company name4",
            "price, RUB": 4,
        },
        {
            "code": "company code2",
            "name": "company name2",
            "price, RUB": 2,
        },
        {
            "code": "company code3",
            "name": "company name3",
            "price, RUB": 3,
        },
    ]
    sorted_data = sorting_dicts(data, "price, RUB")
    assert sorted_data[0]["code"] == "company code4"
    assert sorted_data[1]["code"] == "company code3"
    assert sorted_data[2]["code"] == "company code2"
    assert sorted_data[3]["code"] == "company code1"

    data2 = [
        {
            "code": "company code1",
            "name": "company name1",
            "price_to_earnings, r.u.": 1,
        },
        {
            "code": "company code4",
            "name": "company name4",
            "price_to_earnings, r.u.": 4,
        },
        {
            "code": "company code2",
            "name": "company name2",
            "price_to_earnings, r.u.": 2,
        },
        {
            "code": "company code3",
            "name": "company name3",
            "price_to_earnings, r.u.": 3,
        },
    ]

    sorted_data = sorting_dicts(data2, "price_to_earnings, r.u.")
    assert sorted_data[0]["code"] == "company code1"
    assert sorted_data[1]["code"] == "company code2"
    assert sorted_data[2]["code"] == "company code3"
    assert sorted_data[3]["code"] == "company code4"
