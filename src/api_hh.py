from abc import ABC, abstractmethod
from typing import Any, Union

import requests


class Parser(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __connect_api(self, text: str) -> Any:
        pass

    @abstractmethod
    def get_vacancies(self, text: str) -> list:
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self) -> None:
        """
        Конструктор класса HH
        """

        self.__url: str = "https://api.hh.ru/vacancies"
        self.__headers: dict = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list = []

    def _Parser__connect_api(self, text: str) -> Union[None, Any]:
        """Приватный метод подключения к HH API"""

        self.__params["text"] = text
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)

        if response.status_code != 200:
            return None

        return response

    def get_vacancies(self, text: str) -> list:
        """Метод получения списка вакансий по HH API"""

        response = self._Parser__connect_api(text)
        if response:
            while self.__params.get("page") != 20:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
        return self.__vacancies
