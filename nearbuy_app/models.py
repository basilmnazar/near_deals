from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class register_user(models.Model):
    gender=models.CharField(null=True,max_length=10)
    state=models.CharField(null=True,max_length=30)
    city=models.CharField(null=True,max_length=40)
    phone=models.IntegerField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)