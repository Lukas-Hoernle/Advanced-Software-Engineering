# Advanced-Software-Engineering
Django-project created for the lecture "Advanced software engineering" 

# How to start

## Create virtual environment
```
python -m venv /path/to/new/virtual/environment
```
## Install requirements
```
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
```
## Create a super user
```
DJANGO_SUPERUSER_USERNAME=testuser \
DJANGO_SUPERUSER_PASSWORD=testpass \
DJANGO_SUPERUSER_EMAIL="admin@admin.com" \
python manage.py createsuperuser --noinput
```
## Run server
```
python manage.py runserver
```
