from django.contrib import admin
from .models import ImageUploadModel


# Register your models here.

#필드 정의 pass
@admin.register(ImageUploadModel)
class FaceAdmin(admin.ModelAdmin):
    pass