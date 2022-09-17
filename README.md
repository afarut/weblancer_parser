Weblancer.ner parser
=====================
Эффективно работает в связке с crontab

QUICK START
------------
1. Создайте и активируйте виртуальное окружение:
```console
cd weblancer_parser
python3 -m venv env
source env/bin/activate
```
2. Установите необходимые библиотеки:
```console
python -m pip install -r requirements.txt
```
3. Создайте файл .env и заполните его по образу env_example
4. Далее используйте crontab для запуска программы в определённое время