from typing import Any
from unittest.mock import MagicMock, patch

from src.api_hh import HH, Parser


@patch("src.api_hh.requests.get")
def test_HH_connect_api(mock_data: Any) -> None:
    query = HH()

    status_code = MagicMock()
    status_code.status_code = 200
    status_code.return_value = [{}]

    mock_data.return_value = status_code

    response: Any = query.connect_api("Text")

    assert response.return_value == [{}]


@patch("src.api_hh.requests.get")
def test_HH_connect_api_invalid(mock_data: Any) -> None:
    query = HH()
    response = query.connect_api("Text")

    status_code = MagicMock()
    status_code.status_code = 100

    mock_data.return_value = status_code

    assert response is None


@patch("src.api_hh.HH.connect_api")
def test_test_HH_get_vacancies(mock_data: Any) -> None:
    mock_data.return_value.json.return_value = {"items": [{}, {}]}
    query = HH()
    result = query.get_vacancies("Test")

    assert result == [{}, {}]


@patch("src.api_hh.HH.connect_api")
def test_test_HH_get_vacancies_invalid(mock_data: Any) -> None:
    mock_data.return_value = None

    query = HH()
    result = query.get_vacancies("Test")

    assert result == []


def test_parser() -> None:
    class Test(Parser):

        def connect_api(self, text: str) -> Any:
            pass

        def get_vacancies(self, text: str) -> Any:
            pass

    test = Test()
    Parser.connect_api(test, "Text")
    Parser.get_vacancies(test, "Text")
