from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    #MODIFICAR TITULO SITIO ADMIN
    verbose_name ="The Garden"
