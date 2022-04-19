# from turtle import home
from django.contrib import admin
from django.urls import path

from .views import *

app_name = 'Custom_users'

urlpatterns = [
   path('',PatientSignUpView,name='patientRegister'),
   path('home/',home,name='home'),
   path('profile/', profile, name='profile'),

    path('profile-edit/', profile_edit, name='profile-edit'),

    path('orders-by-user/', orders_by_user, name='orders-by-user'),

    path('filtered-reports-by-user/<int:id>/', filtered_report, name='filtered-reports-by-user')

]