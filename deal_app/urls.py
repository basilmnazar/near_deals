from django.urls import path
from .views import *

urlpatterns =[
   path('deal_register',deal_register,name='deal_register'),  
   path('dealer_index',dealer_index,name='dealer_index'),  
   path('dealer_login',dealer_login,name='dealer_login'),  
   path('',index_main,name='index_main'),
   path('add_fields',add_fields,name='add_fields'), 
  
]