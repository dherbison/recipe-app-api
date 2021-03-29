#docker-compose run app sh -c "python manage.py createsuperuser"
# DID NOT WORK
#
# DO...
docker-compose run app sh -c "python manage.py shell"
# then run
# from django.contrib.auth import get_user_model
# User = get_user_model()
# # user whatever you want for user/pw
# User.objects.create_superuser('danielherbison@gmail.com', 'Edenreal')
