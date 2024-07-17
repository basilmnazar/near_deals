from django.db import models
from django.contrib.auth.models import User
from datetime import time
from django.core.exceptions import ValidationError

def validate_time_format(value):
  try:
    # Assuming your time fields are TimeFields
    time.fromisoformat(value)  # Attempt conversion (ISO format)
  except ValueError:
    raise ValidationError('Invalid time format. Use HH:MM format.')

# Create your models here.

class register_dealer(models.Model):
    merchant_name = models.CharField(max_length=255)
    merchant_type=models.CharField(null=True,max_length=30)
    merchant_address=models.CharField(null=True,max_length=30)
    city=models.CharField(null=True,max_length=40)
    phone=models.IntegerField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)


class model_add_fields(models.Model):
  item_name = models.CharField(max_length=255, null=True,blank=True)
  description = models.TextField(null=True, blank=True)
  start_time = models.TimeField() 
  end_time = models.TimeField()  # Add validator
  item_img = models.ImageField(upload_to='images/', blank=True)  # Assuming image storage