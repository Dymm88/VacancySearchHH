import requests

from config import HEADERS
from params import companies


def put_in_black_list(vacancy_list):
    """
    Функция для добавления компаний в черный список.

    :param vacancy_list: Список компаний
    :return: Объект генератора ответов на запросы на добавление в черный список
    """
    for name in vacancy_list:
        if name['employer']['name'] in companies:
            requests.put(url=f'https://api.hh.ru/vacancies/blacklisted/{name['id']}', headers=HEADERS)


def get_black_list():
    """
    Функция для получения черного списка компаний.

    :return: Объект генератора идентификаторов компаний в черном списке
    """
    url = 'https://api.hh.ru/vacancies/blacklisted'
    r = requests.get(url=url, headers=HEADERS)
    black_list = (t['id'] for t in r.json()['items'])
    return list(black_list)
