
from django.db import models

# Create your models here.

class Voice(models.Model) :
    id = models.CharField(max_length=20,primary_key=True)
