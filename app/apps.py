# from django.apps import AppConfig


# class AppConfig(AppConfig):
#     name = 'app'
    
from django.apps import AppConfig
from django.db.models import BigAutoField

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    label= 'app'

