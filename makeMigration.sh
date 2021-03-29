app=$1
docker-compose run --rm app sh -c "python manage.py makemigrations ${app}"
