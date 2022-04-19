from django import forms
from django.forms import TextInput

from .models import CustomerProfile


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile

        fields = ['profile_name', 'image', 'contact_no', 'address']

        widgets = {
            'profile_name': TextInput(attrs={'class': 'form-control'}),
            'contact_no': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
        }
