from django.db import models

# Create your models here.
class User(models.Model) :
    id = models.CharField(max_length=20,primary_key=True)  #기본키 설정 
    pass1 = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    gender = models.IntegerField(default=0)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    picture = models.CharField(max_length=200)

    def __str__(self):
        return self.id + ":" + self.name+":"+self.pass1

# 이미지 업로드를 위한 모델 생성(데이터베이스와 연결용)
class ImageUploadModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to="images/%Y/%m/%d")
    uploaded = models.DateTimeField(auto_now_add=True)