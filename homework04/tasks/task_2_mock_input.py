"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


#>>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import requests


def connection_to_URL(url):
    try:
        return requests.get(url)
    except BaseException:
        raise ValueError(f"Unreachable {url}")


def establishing_connection(url: str) -> int:
    web_url = connection_to_URL(url)
    res_code = web_url.status_code
    return f"HTTP code: {res_code}"


def count_dots_on_i(url: str) -> int:
    web_url = connection_to_URL(url)
    read_data = web_url.content.decode()
    count_dots = read_data.count("i")
    return count_dots


if __name__ == "__main__":
    print(count_dots_on_i("https://example.com/"))

    print(establishing_connection("https://example.com/"))


