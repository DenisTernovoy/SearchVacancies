def filter_vacancies(list_vacancies: list, filter_words: list) -> list:
    """Функция, которая фильтрует вакансии по ключевому слову в ее наименовании или в ее требованиях"""

    if filter_words:
        filtered_list = []
        for vac in list_vacancies:
            for word in filter_words:
                if word.lower() in vac.name.lower() or word.lower() in vac.requirements.lower():
                    filtered_list.append(vac)
                    continue
    else:
        filtered_list = list_vacancies

    return filtered_list


def get_vacancies_by_salary(list_vacancies: list, range_salary: str = "0 - 9999999999") -> list:
    """Функция, которая фильтрует вакансии по зарплате"""

    if range_salary == "":
        min_salary, max_salary = 0, 9999999999
    else:
        min_salary, max_salary = map(int, range_salary.split(" - "))

    list_vacancies = [vac for vac in list_vacancies if vac.salary["currency"] == "RUR"]
    filtered_list = [vac for vac in list_vacancies if min_salary <= vac <= max_salary]

    return filtered_list


def sort_vacancies(list_vacancies: list) -> list:
    """Функция, сортирующая вакансии по уровню зарплаты"""

    return sorted(list_vacancies, key=lambda x: x.salary["amount"], reverse=True)


def get_top_vacancies(list_vacancies: list, top: int) -> list:
    """Функция возвращающая срез от списка вакансий"""

    return list_vacancies[:top]


def print_vacancies(list_vacancies: list) -> None:
    """Функция выводящая топ вакансий в консоль"""

    for vac in list_vacancies:
        text = (
            f"Вакансия: {vac.name}, зарплата: {vac.salary["amount"]}, адрес: {vac.address}, ссылка: {vac.url_vacancy}"
        )
        print(text)
