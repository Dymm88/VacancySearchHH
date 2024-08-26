# Скрипт для поиска и отклика на вакансии на ресурсе hh.ru

### Для использования необходимо:

1. Зарегистрироваться на сайте https://hh.ru
2. Зарегистрировать приложение на сайте https://dev.hh.ru/
3. Создать проект
4. Активировать виртуальное окружение
5. Клонировать репозиторий `git clone https://github.com/Dymm88/SearchVacanciesHH`
6. Применить зависимости `pip install -r requirements.txt`
7. Создать файл `.env` в корневой папке проекта
8. Поместить в этот файл **CLIENT_ID**, **CLIENT_SECRET**, **REDIRECT_URI**, **TOKEN**, **REFRESH_TOKEN**, **EMAIL** и 
   **RESUME_ID**
9. В файле `access_token.py` получить токен или (при необходимости) обновить его (срок жизни токена - 2 недели)
10. В файле `params.py` можно задать фильтры исходя из личных предпочтений, значения можно взять из официальной
   документации (сейчас указаны параметры для примера)
11. Создать файл `message.py`, в нем разместить сопроводительное письмо и присвоить его константе **MESSAGE_TEXT**
12. Запуск осуществляется командой `python main.py` в терминале

## Ссылка на официальную документацию https://github.com/hhru/api