from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

#안면인식을 위한 기능
class FaceConfig(AppConfig):
    name = "face"