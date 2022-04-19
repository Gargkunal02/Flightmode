from django.contrib import admin

from Doctor_user.models import DoctorProfile

# Register your models here.
class DProfileAdmin(admin.ModelAdmin):
    """Customizing Admin Interface"""
    list_display = [ 'user', 'profile_name', 'contact_no', 'address']
    list_display_links = ['user']
    list_editable = ['profile_name', 'contact_no', 'address']
    # list_filter = ['user']
    search_fields = ['id', 'user', 'contact_no']


# Registering databases
admin.site.register(DoctorProfile, DProfileAdmin)