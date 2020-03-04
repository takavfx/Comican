# Feature
Django practice project.
Manage Library with tagingging each page.

# Development

1. Create virtualenv and activate
    ```bash
    python -m venv .venv
    .venv/Scripts/activate
    ```
2. Install requirements
    ```bash
    pip install -r requirements.txt
    ```
3. Django migrations
    ```bash
    python manage.py makemigrations comican
    python manage.py migrate
    python manage.py createsuperuser
    ```
4. Run development server
    ```
    python manage.py runserver
    ```
