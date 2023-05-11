# scrapy_parser_pep
Асинхронный парсер собирающий данные о PEP с сайта https://www.python.org/.
С каждой страницы PEP парсер собирает номер, название, статус и сохраняет несколько файлов в формате .csv в папке results/...:

## Описание
Парсер документации Python позволяет пользователю получить информацию o PEP, выводя ее в 2 csv файла.
1. Список PEP (номер, название и статус);
2. Общее количество каждого статуса и сумму всех статусов.

## Технологии: 
Python, Scrapy

## Как запустить:
1. Склонируйте репозитоорий
2. Создайте и активируйте виртуальное окружение:
3. Обновите pip и установите зависимости:
4. Запустите паука 'pep' в командной строке: <b>scrapy crawl pep</b>



