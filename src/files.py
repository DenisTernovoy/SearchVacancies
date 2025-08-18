import json
import pathlib
from abc import ABC, abstractmethod


class FileWork(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_data(self) -> list:
        pass

    @abstractmethod
    def write_data(self, dict_data: list) -> None:
        pass

    @abstractmethod
    def delete_data(self, vacancy: dict) -> None:
        pass


class JSONSaver(FileWork):
    """Класс для работы с JSON файлами"""

    file_name: str

    def __init__(self, file_name: str = "vacancies.json") -> None:
        """Конструктор класса JSONSaver"""

        self.__file_name = file_name

    def get_data(self) -> list:
        """Функция, возвращающая список словарей из файла JSON"""

        path = str(pathlib.Path(__file__).parents[1] / "data/" / self.__file_name)

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def write_data(self, dict_data: list) -> None:
        """Функция, записывающая список словарей в файл JSON"""

        path = pathlib.Path(__file__).parents[1] / "data/" / self.__file_name

        if path.exists():
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)

            for vac in dict_data:
                for vac_json in data:
                    if vac["url"] == vac_json.get("url", None):
                        continue
                data.append(vac)
        else:
            data = []

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def delete_data(self, vacancy: dict) -> None:
        """Функция, удаляющая вакансию из списка словарей в JSON"""

        path = str(pathlib.Path(__file__).parents[1] / "data/" / self.__file_name)

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        data = [i for i in data if i.get("url") != vacancy["url"]]

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
