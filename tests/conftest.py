import pytest

from src.vacancies import Vacancy


@pytest.fixture()
def vacancy_1() -> Vacancy:
    return Vacancy(
        "Микробиолог",
        "https://some_url.ru",
        {"currency": "RUR", "from": 100000.0, "to": None},
        "Опыт работы от 3-х лет в лаборатории",
        "Москва",
    )


@pytest.fixture()
def vacancy_2() -> Vacancy:
    return Vacancy(
        "Химик",
        "https://some_url.ru",
        {"currency": "RUR", "from": 80000.0, "to": None},
        "Опыт работы от 3-х лет в лаборатории",
        "Москва",
    )


@pytest.fixture()
def vacancy_3() -> Vacancy:
    return Vacancy(
        "Designer",
        "https://some_url.ru",
        {"currency": "USD", "from": 3000.0, "to": None},
        "Опыт работы от 3-х лет",
        "Москва",
    )


@pytest.fixture()
def vacancy_invalid() -> Vacancy:
    return Vacancy(
        "Designer",
        "https://some_url.ru",
        None,
        None,
        "Москва",
    )


@pytest.fixture()
def list_vacancies() -> list:
    list_vacancy = [
        Vacancy(
            "Микробиолог",
            "https://some_url.ru",
            {"currency": "RUR", "from": 100000.0, "to": None},
            "Опыт работы от 3-х лет в лаборатории",
            "Москва",
        ),
        Vacancy(
            "Химик",
            "https://some_url.ru",
            {"currency": "RUR", "from": 80000.0, "to": None},
            "Опыт работы от 1 года в лаборатории",
            "Москва",
        ),
        Vacancy(
            "Аналитик", "https://some_url.ru", {"currency": "RUR", "from": 150000.0, "to": None}, "Знание НД", "Москва"
        ),
    ]

    return list_vacancy


@pytest.fixture()
def hh_list_vacancies() -> list:
    result = [
        {
            "name": "Микробиолог",
            "alternate_url": "https://some_url.ru",
            "salary": {"currency": "RUR", "from": 100000.0, "to": None},
            "snippet": {"requirement": "Опыт работы от 3-х лет в лаборатории"},
            "area": {"name": "Москва"},
        },
        {
            "name": "Химик",
            "alternate_url": "https://some_url.ru",
            "salary": {"currency": "RUR", "from": None, "to": 80000.0},
            "snippet": {"requirement": "Опыт работы от 1 года в лаборатории"},
            "area": {"name": "Москва"},
        },
        {
            "name": "Аналитик",
            "alternate_url": "https://some_url.ru",
            "salary": {"currency": "RUR", "from": 100000.0, "to": 200000.0},
            "snippet": {"requirement": "Знание НД"},
            "area": {"name": "Москва"},
        },
    ]

    return result


@pytest.fixture()
def dict_list_vacancies() -> list:
    result = [
        {
            "name": "Микробиолог",
            "url": "https://some_url.ru",
            "salary": {"currency": "RUR", "amount": 100000.0},
            "requirements": "Опыт работы от 3-х лет в лаборатории",
            "address": "Москва",
        },
        {
            "name": "Химик",
            "url": "https://some_url.ru",
            "salary": {"currency": "RUR", "amount": 80000.0},
            "requirements": "Опыт работы от 1 года в лаборатории",
            "address": "Москва",
        },
        {
            "name": "Аналитик",
            "url": "https://some_url.ru",
            "salary": {"currency": "RUR", "amount": 150000.0},
            "requirements": "Знание НД",
            "address": "Москва",
        },
    ]

    return result
