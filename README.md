# scrapy_parser_pep
Асинхронный парсер собирающий данные о PEP с сайта https://www.python.org/.
С каждой страницы PEP парсер собирает номер, название, статус и сохраняет несколько файлов в формате .csv в папке /results/:

## Описание
Парсер документации Python позволяет пользователю получить информацию o PEP, выводя ее в 2 csv файла.
1. Список PEP (номер, название и статус);
2. Общее количество каждого статуса и сумму всех статусов.

## Технологии: 
Python, Scrapy

## Как запустить:
1. Склонируйте репозитоорий <br/> 
<b>git@github.com:webbzet/scrapy_parser_pep.git</b>
3. Создайте и активируйте виртуальное окружение: <br/> 
<b>python -m venv venv <br/>
source venv/Scripts/activate</b>
4. Обновите pip и установите зависимости: </br>
<b>python -m pip install --upgrade pip</br>
pip install -r requirements.txt</b>

4. Запустите паука 'pep' в командной строке: <br> <b>scrapy crawl pep</b>



