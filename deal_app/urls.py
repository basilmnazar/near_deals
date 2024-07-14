from django.urls import path
from .views import *

urlpatterns =[
   path('deal_register',deal_register,name='deal_register'),  
    
]