import requests

from black_list import get_black_list, put_in_black_list
from config import HEADERS, RESUME_ID
from message import MESSAGE_TEXT


def get_vacancies(params):
    vacancy_list = []
    url = 'https://api.hh.ru/vacancies'
    while True:
        r = requests.get(url=url, headers=HEADERS, params=params)
        items = r.json()['items']
        vacancy_list += items
        if r.json()['pages'] == params['page'] + 1:
            break
        params['page'] += 1
    return vacancy_list


def vacancy_ids(vacancy_list):
    vacancy_list_id = [vacancy['id'] for vacancy in vacancy_list]
    put_in_black_list(vacancy_list)
    ended_vacancy_list = list(set(vacancy_list_id) - set(get_black_list()))
    return ended_vacancy_list


def response_vacancies(list_vacancies):
    success = 0
    for item in list_vacancies:
        r = requests.post(
            f'https://api.hh.ru/negotiations?resume_id={RESUME_ID}&vacancy_id={str(item)}&message={MESSAGE_TEXT}',
            headers=HEADERS,
        )
        match r.status_code:
            case 201:
                success += 1
                print(f'Резюме успешно отправлено на вакансию {item}')
            case 200:
                print(f'Необходимо выполнение задания на вакансию {item}')
            case _:
                print(f'Произошла ошибка при отправке на вакансию {item}: {r.status_code}')
    print(f'Количество отправленных отзывов - {success}')
