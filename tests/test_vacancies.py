import pytest

from src.vacancies import Vacancy


def test_vacancy(vacancy_1: Vacancy) -> None:
    assert vacancy_1.name == "Микробиолог"
    assert vacancy_1.url_vacancy == "https://some_url.ru"
    assert vacancy_1.salary == {"currency": "RUR", "amount": 100000.0}
    assert vacancy_1.requirements == "Опыт работы от 3-х лет в лаборатории"
    assert vacancy_1.address == "Москва"


def test_vacancy_compare(vacancy_1: Vacancy, vacancy_2: Vacancy) -> None:
    assert (vacancy_1 > vacancy_2) is True
    assert (vacancy_1 >= vacancy_2) is True
    assert (vacancy_1 < vacancy_2) is False
    assert (vacancy_1 <= vacancy_2) is False
    assert (vacancy_1 >= 10000) is True
    assert (vacancy_1 <= 200000) is True
    assert (vacancy_2 >= 10000) is True
    assert (vacancy_2 <= 100000) is True


def test_vacancy_compare_invalid(vacancy_1: Vacancy, vacancy_3: Vacancy) -> None:
    with pytest.raises(ValueError) as error:
        vacancy_1 >= vacancy_3
        assert str(error.value) == "Сравниваемые вакансии должны иметь одинаковую валюту"


def test_vacancy_compare_invalid_1(vacancy_1: Vacancy) -> None:
    with pytest.raises(TypeError) as error:
        vacancy_1 >= "str"
        assert str(error.value) == "Сравниваемы объекты должны принадлежать классу Vacancy или float/int"


def test_vacancy_cast_to_object_list(hh_list_vacancies: list) -> None:
    result = Vacancy.cast_to_object_list(hh_list_vacancies)
    assert len(result) == 3
    assert all(isinstance(x, Vacancy) for x in result)


def test_vacancy_cast_to_dict_format(list_vacancies: list, dict_list_vacancies: list) -> None:
    assert Vacancy.cast_to_dict_format(list_vacancies) == dict_list_vacancies


def test_vacancy_validate_salary(vacancy_invalid: Vacancy) -> None:
    assert vacancy_invalid.salary == {"currency": None, "amount": 0}


def test_vacancy_validate_requirements(vacancy_invalid: Vacancy) -> None:
    assert vacancy_invalid.requirements == ""
