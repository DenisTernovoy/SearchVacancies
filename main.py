import pathlib

import requests
import pprint
from src.api_hh import HH
from src.files import JSONSaver
from src.vacancies import Vacancy


def connect() -> int:
    hh_connect = HH()
    hh_vacancies = hh_connect.get_vacancies("Микробиолог")
    list_vacancies = Vacancy.cast_to_object_list(hh_vacancies)
    list_dict_format = Vacancy.cast_to_dict_format(list_vacancies)
    js = JSONSaver()
    js.write_data(list_dict_format)


connect()

