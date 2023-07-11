# Scrapy Parser PEP
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://scrapy.org/)

> Парсер создан c помощью фреймворка "Scrapy", который собирает данные обо всей PEP документации так необходимой в нашей с Вами деятельности, а также создаёт два файла:
> - Первый файл содержит название, статус и номер документа.
> - Второй файл содержит общее количество полученных документов и их статусов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Sobodazh/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить команду:

```
scrapy crawl pep
```
