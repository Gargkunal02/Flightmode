from django.contrib import admin

# from Custom_users.models import CustomerProfile
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = [ 'user', 'profile_name', 'contact_no', 'address']
    list_display_links = ['user']
    list_editable = ['profile_name', 'contact_no', 'address']
    # list_filter = ['user']
    search_fields = ['id', 'user', 'contact_no']

class Useradmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','is_patient','is_doctor','is_lab')

# Registering databases
admin.site.register(CustomerProfile, ProfileAdmin)
admin.site.register(User,Useradmin)