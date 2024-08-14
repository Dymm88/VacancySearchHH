params_SPb = {  # параметры для поиска вакансий в SPb
    'page': 0,
    'per_page': 100,
    'text': 'python -преподаватель -ментор',
    'experience': 'noExperience',
    'area': 2,
    'period': 14,
    'archived': False,
}

params_All = {  # параметры для поиска вакансий по РФ
    'page': 0,
    'per_page': 100,
    'text': 'python -преподаватель -ментор',
    'experience': 'noExperience',
    'area': 113,
    'period': 14,
    'archived': False,
    "schedule": "remote",
}

companies = (  # список компаний, которые нужно добавить в blacklist
    'Aston',
    'яндекс Крауд',
    'Яндекс Крауд: Поддержка',
    'Rebotica',
    'Яндекс',
    'ИнфоТеКС',
    'АйТи-Солюшн',
)
