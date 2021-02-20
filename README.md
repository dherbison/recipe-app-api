# recipe-app-api
Recipe App API Source Code

## Requirements
    Case is VERY important here. This caused me issues:
        Djangorestframework>=3.12.2,<3.13.0 should have been djangorestframework>=3.12.2,<3.13.0

## Travis CI
    Sign in with GITHUB account (travis-ci.org soon to be travis-ci.com).

## GitHUB
    Use GIT_CURL_VERBOSE=1 to see what SSH is upto when something like "git push" does not work.

## Flake8
    Lint Tool

## Test
* All test files must begin with the word "test"
* All test cases must begin with the word "test".
* see the runTest script to run test.

## Docker
### Create app
docker-compose run --rm app sh -c "python manage.py startapp core".  The "--rm" is optional.
### Build app
docker-compose build
### Create Super User
The command _**docker-compose run app sh -c "python manage.py createsuperuser"**_, DID NOT WORK.

So i ran:
* _**docker-compose run app sh -c "python manage.py shell"**_

then typed in, when the shell opened:
* from django.contrib.auth import get_user_model
* User = get_user_model()
* User.objects.create_superuser('danielherbison@gmail.com', 'Edenreal')

use whatever you want for user/pw.
### Create DB (Migration)
docker-compose run app sh -c "python manage.py makemigrations core"
### Run Test
docker-compose run app sh -c "python manage.py test && flake8"
### Start 
docker-compose up

## Database
### Creation
* create table, see models.py
* run migrations, see makeMigration
* model will appear under migrations dir.
* if you change model, the run migrations.
* SQLLITE is used by default

  
## Files
* if \_\_init\_\_.py is missing from a dir, python will ignore that dir.

