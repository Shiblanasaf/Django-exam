from django.db import models



# Create your models here.
class Jobs(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    designation=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()