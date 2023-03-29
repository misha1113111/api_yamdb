Cоздать и активировать виртуальное окружение:
python3 -m venv venv
* Если у вас Linux/macOS
source venv/bin/activate
Если у вас windows
source venv/scripts/activate
python3 -m pip install --upgrade pip
Установить зависимости из файла requirements.txt:
pip install -r requirements.txt
Выполнить миграции:
python3 manage.py migrate
Запустить проект:
python3 manage.py runserver

Чтобы загрузить данные из определённого файла для конкретной модели, выполните команду:
python3 manage.py load_data_csv --path <путь к csv-файлу> --model_name <имя модели> --app_name <название приложения>

Например:
python3 manage.py load_data_csv --path static/data/users.csv --model_name user --app_name users

Данные из файлов необходимо загружать в следующем порядке:
* users.csv
* genre.csv
* category.csv
* titles.csv
* genre_title.csv
* review.csv
* comments.csv