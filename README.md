# This is a project boilerplate for Django to deploy a secure Django project on any web hosting site.

### Any commands with "$" at the beginning run on cmd/terminal of your local machine

# Please install virtualenv on your local computer
$ pip install virtualenv

### This is what I like do when creating a virtual environment (you can change whatever you like)
(I always like to called the virtual environment as venv)
# Creating virtual environment

$ virtualenv venv

$ cd venv

## For Windows
$ scripts\activate

## For Linux
$ source bin\activate

$ cd ..

## Installing requirements

$ cd src

$ pip install -r requirements-dev.txt

### And for production environment

$ pip install -r requirements-prod.txt


Then I create the django project.

$ django-admin startproject project_name

## But anyone who use this boilerplate will already create a project called mysite which is inside the src folder

# Custom management command
A management custom command added to rename project name and all the related places where changes must be done to run the project.
## For changing the project name run the following command.
$ python manage.py rename project_name

so current folder structure would be like this...

django-project-boilerplate(project folder)

--.git

--src(root folder)

----core

----mysite

----manage.py

----(...)

--venv

--README.md

--LICENSE

For security purpose this boilerplate uses python-decouple to secure all sensitive variables like SECRECT_KEY, Production level database username, password etc to a secure file called .env

## A example of the .env file given as .env.example

### For local development you can rename the .env.example file to .env to run the project on local computer.

# Deploying
There are two instruction file(project folder) on how to deploy django projects on heroku and digital ocean (I am continuously updating these to file) and more like AWS and others will be added in the future.

The boilerplate can be improved so please let me know how to improve...
# Lets talk about project structure of the src(source) folder
In the src folder there are three apps already created by default
1. core
2. pages
3. accounts

# Core app
Django suggest if any custom command has to create for a project it should be on the core > management > command folder.
Like I created the rename command

# Pages app
I created the pages app to handle the main pages like index(home), about, contact etc for now.
Also I created the placeholder pages in the template folder of the pages folder.

# Accounts app
I created the accounts app to handle the pages like login, register, dashboard etc for now.
Also I created the placeholder pages in the templates folder of the accounts folder.

# Lets talk about the settings of the project
src > mysite > settings
There are three file
1. base.py
2. developement.py
3. production.py

base.py file has contain things that both needed for both development and production settings.

# Development settings
Development settings included Django debug tools and which is helpful for debugging a Django project.

# Production settings
Production settings I configured Database to use PostgreSQL so to secure the database sensitive information like DB_NAME,  DB_USER, DB_PASSWORD etc I use the python-decouple module.

By default python-decouple check for .env file for sensitive information of the project.

### This .env file should not be push on the public repository. You can create variable on the hosting site so just created their will auto fetch value by python-decouple module.

Checkout the .env.example file to create a .env file

# Note .env.example file contain the Django project SECRET_KEY and it's just a 50 character long random number so you change it when you use this boilerplate.

# Final instruction
If anyone want to change the project to use the production settings just change one place only.

# Edit manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.development')
to
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.production')
