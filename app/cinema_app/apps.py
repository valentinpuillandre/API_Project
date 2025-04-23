from django.apps import AppConfig


class CinemaAppConfig(AppConfig):
    default_auto_field = 'django_mongodb_backend.fields.ObjectIdAutoField'
    name = 'cinema_app'
