### Motivation
After learning online, I added login and decided to share.

todo features:
* ability to register and logged in [added]
* add toto by user [improved]
* display todo by user and sorted by due-date [improved]
* delete own todo after it's done [improved]

### Install Guide
copy and run (assume linux with python3):
```
python3 -m venv test
cd test
source bin/activate
git clone https://github.com/wendy-py/django_todo.git
cd django_todo
pip install Django django-crispy-forms
pip install --upgrade attrs
python manage.py migrate
python manage.py runserver
```
