from unittest import TestCase

import requests_mock
from homework04.tasks.task_2_mock_input import *


class TestHTTPRequest(TestCase):
    def test_connection_to_URL(self):
        with requests_mock.Mocker() as mock_request:
            mock_request.get("http://fake-html.com", text="Some html formatted text")
            response = connection_to_URL("http://fake-html.com")

        assert response.text == "Some html formatted text"

    def test_connection_to_URL_error(self):
        with self.assertRaises(ValueError):
            connection_to_URL("http://123564353$$$$$$$.com")

    def test_count_dots_on_i(self):
        with requests_mock.Mocker() as mock_request:
            mock_request.get("http://fake-html.com", text="iiiii_iiiii")
            text = count_dots_on_i("http://fake-html.com")

        assert text == 10

    def test_establishing_connection(self):
        with requests_mock.Mocker() as mock_request:
            mock_request.get("http://fake-html.com", text="Hello!", status_code=404)
            res_code = establishing_connection("http://fake-html.com")

        assert res_code == "HTTP code: 404"
