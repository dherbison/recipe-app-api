# recipe-app-api
Recipe App API Source Code

## Requirements
    Case is VERY important here. This caused me issues:
        Djangorestframework>=3.12.2,<3.13.0 should have been djangorestframework>=3.12.2,<3.13.0

## Travis CI
    Sign in with GITHUB account (travis-ci.org soon to be travis-ci.com).

## GitHUB
    Use GIT_CURL_VERBOSE=1 to see what SSH is upto when something like "git push" does not work.

## Flake7
    Lint Tool

## Test
* All test files must begin with the word "test"
* All test cases must begin with the word "test".
* see the runTest script to run test.

## Create app
docker-compose run app sh -c "python manage.py startapp core"

## Database creation
* create table, see models.py
* run migrations, see makeMigration
* model will appear under migrations dir.
* if you change model, the run migrations.

## Files
* if \_\_init\_\_.py is missing from a dir, python will ignore that dir.