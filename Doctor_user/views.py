from django.shortcuts import render,redirect

# Create your views here.
from .models import *
from Custom_users.models import User 
from Custom_users.urls import *

def DocotrSignUpView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # Month_of_Pregnancy = request.POST['Month_of_Pregnancy']
        age = request.POST['age']
        contact_no = request.POST['phone_number']
        gender = request.POST['gender']
        address = request.POST['address']
        hospital = request.POST['hospital']
        years_of_experience = request.POST['years_of_experience']
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'Login/rr.html', {'message': 'Email already registered.'})
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.is_doctor = True
            user.save()
            doctor = DoctorProfile(user=user)
            doctor.age = age
            doctor.contact_no = contact_no
            doctor.gender = gender
            doctor.address = address
            doctor.hospital = hospital
            doctor.years_of_experience = years_of_experience
            # patient.pregnancy_month = Month_of_Pregnancy
            doctor.save()
            return redirect('Custom_users:home')
            # return render(request, 'portal/patient_home.html')
    return render(request, 'Login/rr.html')