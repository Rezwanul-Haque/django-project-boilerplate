# Django Deployment to Heroku

## In this guide I will go through all the steps to deploy a Django application on Heroku.

# Any commands with "$" at the beginning run on cmd/terminal of your local machine

### Create A Heroku Account

### Login Heroku Account

### Install heroku-cli installer

# Now you can access Heroku commands in the terminal or Cmd
$ heroku login

## Press any key web browser will open and their will log in to your heroku account.
## Cmd automatically logged in to your heroku account after that.

### or

# If you want stay with the cmd for login to heroku.
$ heroku login -i

# Clone your git repo
$ git clone https://user_name@bitbucket.org/username/project_name.git
$ cd project_name

### Prerequisite
## Procfile (name case is important) in project root
## requirements.txt  ## Hold all the Python and Django modules needed for the project.
## Add Gunicorn, whitenoise, dj-database-url to requirements.txt;
## A runtime.txt to specify the correct Python version in the project root;

# >> Procfile
web: gunicorn mysite.wsgi --log-file -

# >> requirements.txt
1. Django==version
2. python-decouple==version
3. psycopg2==version
4. psycopg2-binary==version
5. pillow==version
6. gunicorn==version
7. whitenoise==version
8. dj-database-url==version

## or A handy shortcut
$ pip freeze > requirements.txt
## This way all packages in your virtual environment will added to requirements.txt with packages and their dependencies.
### So you have clean up the files accordingly.

## The WhiteNoise middleware should be placed directly after the Django SecurityMiddleware
'whitenoise.middleware.WhiteNoiseMiddleware',

# Create a heroku new application
$ heroku create app_name

## You can omit the app name parameter (in my case, app_name), then Heroku will pick a name for you.

# Add a PostgreSQL database to your app:
$ heroku addons:create --app app_name heroku-postgresql:hobby-dev

### Now login to Heroku Dashboard and access your recently created app
### Inside the Settings tab click on the "Reveal Config Vars" button and add your variables as you would do in the .env file.

# Disable the python manage.py collectstatic command at deploying
$heroku config:set DISABLE_COLLECTSTATIC=1

# Push to deploy
$ git push heroku master

# Migrate the database
$ heroku run python manage.py migrate

# Fetch all apps static files to static_root
$ heroku run python manage.py collectstatic

# If some reason your localapps doesn't automatically migrate so manually migration needed.
$ heroku bash

$ >>> python manage.py makegrations app_name

$ >>> python manage.py migrate app_name migration_number(e.g. 0001)

# Hopefully after this your will live on heroku
## Browser type your web sites url.

App_name.herokuapp.com
