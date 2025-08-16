import requests
import pprint
from src.api_hh import HH
from src.vacancies import Vacancy


def connect() -> int:
    hh_connect = HH()
    hh_vacancies = hh_connect.get_vacancies("Микробиолог")
    list_vacancies = Vacancy.cast_to_object_list(hh_vacancies)
    pprint.pprint(Vacancy.cast_to_dict_format(list_vacancies[5:7]))
    # pprint.pprint(hh_vacancies[1:5])
    a, b = list_vacancies[5:7]
    print(a < 1000000)

connect()

