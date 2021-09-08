# api_yamdb
api_yamdb


# chaplinskiy/api_yamdb

## Описание:

Появится немного позже.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/chaplinskiy/api_yamdb.git
```

```bash
cd api_yamdb/
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
cd api_yamdb/ && python3 manage.py migrate
```

Запустить проект:

```bash
python3 manage.py runserver
```
