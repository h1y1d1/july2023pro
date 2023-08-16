from django.db import models

# Create your models here.

class Demomodel(models.Model):
    name=models.CharField(max_lenght=50)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()


