from django.apps import AppConfig



# class OwnerProfileConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'smartcareProject'

#     def ready(self):
#         import smartcareProject.signals

class smartcareProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smartcareProject'

class AppConfig(AppConfig):
    name = 'app'
    verbose_name = 'Admin Dashboard'



