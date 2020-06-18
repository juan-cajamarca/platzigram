# Platzigram
A Django-based Instagram replica.

## Installing
- Install Python 3
- Build a virtual environment - `python3 -m venv <virtual_environment_folder_name>`
- Open virtual environment - `source <virtual_environment_path>/bin/activate`
- Install Django - `pip install django -U`

## Deployment
- Clone project
- Run migrations - `python3 manage.py migrate`
- Run server - `pythone3 manage.py runserver`
- Look at http://localhost:8000/