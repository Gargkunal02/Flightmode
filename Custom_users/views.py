from django.shortcuts import render, redirect
# from Custom_users.models import *
# from Custom_users.models import CustomerProfile
from .models import User, CustomerProfile
# from Doctor_user.models import * 
# Create your views here.

from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# allauth decorator @verified_email_required
# from allauth.account.decorators import verified_email_required
# from allauth.account.views import SignupView, LoginView, PasswordResetView

from tests.models import TestOrder
from report_processing.models import PaymentValidation

from .forms import ProfileUpdateForm

def PatientSignUpView(request):
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
        password1 = request.POST['password']
        password2 = request.POST['cpassword']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'Login/register.html', {'message': 'Email already registered.'})
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            user.is_patient = True
            user.save()
            patient = CustomerProfile(user=user)
            patient.age = age
            patient.contact_no = contact_no
            patient.gender = gender
            patient.address = address
            # patient.pregnancy_month = Month_of_Pregnancy
            patient.save()
            return redirect('portal:home')
            # return render(request, 'portal/patient_home.html')
    return render(request, 'Login/register.html')


# def home(request):
#     return render(request,'Login/home.html')



# class MySignupView(SignupView):
#     template_name = 'account/custom_users/custom_signup.html'


# class MyLoginView(LoginView):
#     template_name = 'account/login.html'
#
#
# class MyPasswordResetView(PasswordResetView):
#     template_name = 'account/password_reset.html'
#
#
# class MyPasswordChangeView(PasswordResetView):
#     template_name = 'account/password_change.html'


@login_required()
def profile(request, template_name='account/custom_users/profile.html'):
    return render(request, template_name)

########################################################################################


@login_required()
def profile_edit(request, template_name='account/custom_users/profile_edit.html'):
    existing_profile = get_object_or_404(CustomerProfile, user=request.user)
    profile_form = ProfileUpdateForm(instance=existing_profile)

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=existing_profile)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile Updated for {}'.format(request.user.username), extra_tags='html_safe')
            # return redirect('custom_users:profile')
            return redirect('custom_users:orders-by-user')

    context = {
        'profile_form': profile_form,
        'existing_profile': existing_profile,
        }

    return render(request, template_name, context)

########################################################################################


def orders_by_user(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        user_profile = Profile.objects.filter(user=user.id)

        if user_profile:
            profile = get_object_or_404(CustomerProfile, user=request.user.id)

            orders = TestOrder.objects.filter(client_info=profile.id).order_by('-id')

            paginator = Paginator(orders, 5)
            page = request.GET.get('page')
            paginator_data = paginator.get_page(page)

            template = 'account/custom_users/orders_by_user.html'
            context = {'orders': paginator_data}

            return render(request, template, context)

########################################################################################


def filtered_report(request, id=None):
    user = get_object_or_404(User, id=id)

    filtered_reports = PaymentValidation.objects.filter(approved_order__client_info__user=user)

    # Filtered reports Paginator
    paginator = Paginator(filtered_reports, 20)
    page = request.GET.get('page')
    filtered_reports_paginator = paginator.get_page(page)

    template = 'account/custom_users/filtered_reports.html'

    context = {'filtered_reports': filtered_reports_paginator}

    return render(request, template, context)

########################################################################################


