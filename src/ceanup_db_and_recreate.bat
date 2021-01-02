@echo off

setlocal
rmdir /s /y migrations
del db.sqlite3

python manage.py makemigrations comican
python manage.py migrate
python manage.py createsuperuser

endlocal