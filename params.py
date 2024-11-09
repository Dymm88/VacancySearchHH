params_SPb = {  # параметры для поиска вакансий в SPb
    "page": 0,
    "per_page": 100,
    "text": "python NOT преподаватель NOT ментор NOT наставник",
    "experience": "noExperience",
    "area": 2,
    "period": 30,
    "archived": False,
}

params_All = {  # параметры для поиска вакансий по РФ
    "page": 0,
    "per_page": 100,
    "text": "python NOT преподаватель NOT ментор NOT наставник",
    "experience": "noExperience",
    "area": 113,
    "period": 30,
    "archived": False,
    "schedule": "remote",
}

companies = (  # список компаний, id вакансий которых нужно добавить в blacklist
    "Aston",
    "Яндекс Крауд",
    "Яндекс Крауд: Поддержка",
    "Rebotica",
    "Яндекс",
    "ИнфоТеКС",
    "АйТи-Солюшн",
    "EasyCode",
    "Школа математики и программирования Matrix",
)
