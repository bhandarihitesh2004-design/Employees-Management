# eManagement (Django)

Simple Django project with an `employees` app demonstrating CRUD, authentication, and messages.

Run instructions:

1. Create virtualenv and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run migrations, create superuser, load sample data, and start server:

```powershell
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata employees/fixtures/initial_data.json
python manage.py runserver
```

Open http://127.0.0.1:8000/ and login to manage employees.

Author by Hitesh Bhandari