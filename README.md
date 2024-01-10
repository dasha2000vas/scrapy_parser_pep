# scrapy_parser_pep

## Описание
<h4>Этот проект собирает информацию о всех документах pep со страницы https://peps.python.org/ и выводит её в два файла. В одном указываются номер, имя и статус каждого pep, в другом - количесво pep в каждом статусе и их общая сумма. Программа работает на основе фреймворка Scrapy.</h4>

## Как скачать и запустить проект:

1. **Клонировать репозиторий и перейти в папку с ним:**

```bash
git clone git@github.com:dasha2000vas/scrapy_parser_pep.git 
cd scrapy_parser_pep
```

2. **Создать и активировать виртуальное окружение:**

```bash
python -m venv venv
source venv/Scripts/activate
```

3. **Установить зависимости из файла requirements.txt:**

```bash
pip install -r requirements.txt
```

4. **Запустить программу:**
```bash
scrapy crawl pep
```

## Технический стек:
* Scrapy2.5.1
* Twisted22.2.0
