from django.urls import path
from .views import *


urlpatterns =[
    path('',admin_register,name='admin_register'),
    path('admin_login/',admin_login,name='admin_login'),
    path('admin_index',admin_index,name='admin_index'),
]