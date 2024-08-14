import requests

from config import HEADERS
from params import companies


def put_in_black_list(list_companies):
    """
    Функция для добавления компаний в черный список.

    :param list_companies: Список компаний
    :return: список ответов на запросы на добавление в черный список
    """
    black_list = []
    for name in list_companies:
        if name['employer']['name'] in companies:
            r = requests.put(url=f'https://api.hh.ru/vacancies/blacklisted/{name['id']}', headers=HEADERS)
            black_list.append(r)
    return black_list


def get_black_list():
    """
    Функция для получения черного списка компаний.

    :return: Список идентификаторов компаний в черном списке
    """
    url = 'https://api.hh.ru/vacancies/blacklisted'
    black_list = []
    r = requests.get(url=url, headers=HEADERS)
    for t in r.json()['items']:
        black_list.append(t['id'])
    return black_list
