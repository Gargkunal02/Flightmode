from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_lab = models.BooleanField(default=False)

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_name = models.CharField(max_length=250)
    age = models.IntegerField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    secondaryPhoneNumber = models.CharField(max_length=10)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=150, blank=True, null=True)

    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Customer Profiles'

    def __str__(self):
        return self.user.username