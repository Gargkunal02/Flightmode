# from turtle import home
from django.contrib import admin
from django.urls import path

from .views import *

# app_name = 'doc'

urlpatterns = [
   path('doctor/',DocotrSignUpView,name='doctorRegister'),
]