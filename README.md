# Main_Application 
https://resumewade.herokuapp.com/
- Language - Python
- Framework - Django
## Description of Application 
- **Django Application Hosted on Heroku Displaying the Resume of Wade Chriestenson**
## Installation
Use the package manage [pip](https://pip.pypa.io/en/stable/) to install requirements.txt file 
to install all required packages.
```bash
pip install -r requirements.txt
```
***Requirments.txt***
- asgiref==3.5.0
- Django==4.0.3
- django-heroku==0.3.1
- gunicorn==20.1.0
- plotly==5.6.0
- six==1.16.0
- tenacity==8.0.1
- tzdata==2022.1
whitenoise==6.0.0
## ***.gitignore***
- /venv (ignore virtual enviroment directory)
- Base_App/setting.py (config file)
- /manage.py (main run file)
## ***Procfile***
- .txt file to tell Heroku what type of app and where the app entry point is.
## ***Base_App*** - Backend Directory
- __init__.py
- asgi.py - (used for server setting)
- setting.py - (used for the full app settings, security, middleware, static directories, etc..)
- url.py - (used for routing back-end urls) - only has admin panel and front-end urls
- wsgi.py - (used for more server settings)
## ***_config.yml***
- Config file for github-pages. ( themes and config for host)
## ***Resume*** - Front-End Directory.
- __init__.py
- admin.py - (set admin settings for django admin panel)- not in use
- apps.py - (unsure of use) - not in use
- migration - (changes made in the database) -not in use
- models.py - (used for creating database tables and pushes them into the migration directory)
- static - (directory used for holding Images, CSS files, Javascript files and CSV files)
- test.py - (used for writing test for the front-end)
- urls.py - (used for routing all urls in the front end)
- views.py - (used for writing the data that post to the html files) 
- forms.py - (used for createing forms to render to HTML)
## ***templates*** - HTML Directory
- about-me.html
## ***manage.py*** - used to run django app
Use command below to run server on local host to view site in action.
```bash
python manage.py runserver
```
