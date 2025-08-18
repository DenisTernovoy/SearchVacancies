import re
from typing import Any


class Vacancy:
    """Класс для работы с вакансиями"""

    name: str
    url_vacancy: str
    salary: dict
    requirements: str
    address: str

    list_of_obj_vacancies: list = []
    list_of_dict_vacancies: list = []

    __slots__ = ("name", "url_vacancy", "salary", "requirements", "address")

    def __init__(self, name: str, url_vacancy: str, salary: Any, requirements: Any, address: str) -> None:
        """Конструктор для класса Vacancy"""

        self.name = name
        self.url_vacancy = url_vacancy
        self.salary = self.__validate_salary(salary)
        self.requirements = self.__validate_requirements(requirements)
        self.address = address

    def __ge__(self, other: Any) -> bool:
        """Магический метод сравнения >="""

        obj_1, obj_2 = self.__validate_type(self, other)

        return obj_1 >= obj_2

    def __gt__(self, other: Any) -> bool:
        """Магический метод сравнения >"""

        obj_1, obj_2 = self.__validate_type(self, other)

        return obj_1 > obj_2

    def __le__(self, other: Any) -> bool:
        """Магический метод сравнения <="""

        obj_1, obj_2 = self.__validate_type(self, other)

        return obj_1 <= obj_2

    def __lt__(self, other: Any) -> bool:
        """Магический метод сравнения <"""

        obj_1, obj_2 = self.__validate_type(self, other)

        return obj_1 < obj_2

    @classmethod
    def cast_to_object_list(cls, hh_vacancies: list) -> list:
        """Метод класса для преобразования вакансий в объекты класса Vacancy и сохранения их в список"""

        for vacancy in hh_vacancies:
            name = vacancy["name"]
            url = vacancy["alternate_url"]
            salary = vacancy["salary"]
            requirements = vacancy["snippet"]["requirement"]
            address = vacancy["area"]["name"]
            cls.list_of_obj_vacancies.append(Vacancy(name, url, salary, requirements, address))
        return cls.list_of_obj_vacancies

    @classmethod
    def cast_to_dict_format(cls, list_objects: list) -> list:
        """Функция, которая преобразует объект в формат словаря"""

        for vac in list_objects:
            data = {
                "name": vac.name,
                "url": vac.url_vacancy,
                "salary": vac.salary,
                "requirements": vac.requirements,
                "address": vac.address,
            }
            cls.list_of_dict_vacancies.append(data)

        return cls.list_of_dict_vacancies

    @staticmethod
    def __validate_salary(salary_dict: dict) -> dict:
        """Приватный метод для валидации зарплаты"""

        if salary_dict is not None:
            currency = salary_dict["currency"]
            if isinstance(salary_dict, dict):
                if salary_dict["from"] and salary_dict["to"]:
                    salary: float = (int(salary_dict["to"]) + int(salary_dict["from"])) / 2
                elif salary_dict["to"]:
                    salary = salary_dict["to"]
                else:
                    salary = salary_dict["from"]

                return {"currency": currency, "amount": float(salary)}

        return {"currency": None, "amount": 0}

    @staticmethod
    def __validate_requirements(requirements: str) -> str:
        """Метод для валидации (форматирования) требований к работнику"""

        if requirements:
            cleaned_text = re.sub(r"<.*?>", "", requirements)
            return cleaned_text
        return ""

    @staticmethod
    def __validate_type(obj_1: Any, obj_2: Any) -> Any:

        if isinstance(obj_2, obj_1.__class__):
            if obj_2.salary["currency"] != obj_1.salary["currency"]:
                raise ValueError("Сравниваемые вакансии должны иметь одинаковую валюту")
            else:
                return obj_1.salary["amount"], obj_2.salary["amount"]
        elif isinstance(obj_2, (float, int)):
            return obj_1.salary["amount"], obj_2
        else:
            raise TypeError("Сравниваемы объекты должны принадлежать классу Vacancy или float/int")
