from typing import Any

from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, print_vacancies, sort_vacancies


def test_filter_vacancies(list_vacancies: list) -> None:
    result = filter_vacancies(list_vacancies, ["Аналитик"])
    assert result == [list_vacancies[-1]]


def test_filter_vacancies_1(list_vacancies: list) -> None:
    result = filter_vacancies(list_vacancies, [])
    assert result == list_vacancies


def test_get_vacancies_by_salary(list_vacancies: list) -> None:
    result = get_vacancies_by_salary(list_vacancies, "100000 - 150000")
    assert result == [list_vacancies[0], list_vacancies[2]]


def test_get_vacancies_by_salary_1(list_vacancies: list) -> None:
    result = get_vacancies_by_salary(list_vacancies, "")
    assert result == list_vacancies


def test_sort_vacancies(list_vacancies: list) -> None:
    result = sort_vacancies(list_vacancies)
    assert result == [list_vacancies[2], list_vacancies[0], list_vacancies[1]]


def test_get_top_vacancies(list_vacancies: list) -> None:
    assert get_top_vacancies(list_vacancies, 2) == list_vacancies[:2]


def test_print_vacancies(capsys: Any, list_vacancies: list) -> None:
    print_vacancies([list_vacancies[2]])
    message = capsys.readouterr()
    assert message.out == "Вакансия: Аналитик, зарплата: 150000.0, адрес: Москва, ссылка: https://some_url.ru\n"
