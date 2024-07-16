from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class register_dealer(models.Model):
    merchant_name = models.CharField(max_length=255)
    merchant_type=models.CharField(null=True,max_length=30)
    merchant_address=models.CharField(null=True,max_length=30)
    city=models.CharField(null=True,max_length=40)
    phone=models.IntegerField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


class model_add_fields(models.Model):
    item_name=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    start_time = models.DateTimeField()  # Using DateTimeField for date and time
    end_time = models.DateTimeField()
    item_img=models.ImageField(upload_to='images/',null=True,blank=True)
