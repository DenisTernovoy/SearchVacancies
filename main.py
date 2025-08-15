import requests

from src.api_hh import HH


def connect() -> int:
    hh_connect = HH()
    hh_vacancies = hh_connect.get_vacancies("Микробиолог")
    print(hh_vacancies, sep='\n')

print(connect())
