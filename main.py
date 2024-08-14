from params import params_SPb, params_All
from vacancies import get_vacancies, vacancy_ids, response_vacancies


def main():
    data_spb = get_vacancies(params_SPb)
    list_vacancies = vacancy_ids(data_spb)
    response_vacancies(list_vacancies)
    data_all = get_vacancies(params_All)
    list_vacancies = vacancy_ids(data_all)
    response_vacancies(list_vacancies)


if __name__ == '__main__':
    main()
