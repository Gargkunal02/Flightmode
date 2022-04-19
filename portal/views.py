from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import login, authenticate

from tests.models import Test, TestCategory

def home(request):
    all_tests = Test.objects.all()
    all_category = TestCategory.objects.all().order_by('-id')

    query = request.GET.get('q')

    if query:
        all_tests = all_tests.filter(Q(test_name__icontains=query)).distinct()

    paginator = Paginator(all_tests, 12)
    page = request.GET.get('page')
    all_tests_paginator_data = paginator.get_page(page)

    template = 'violet-master/index.html'

    context = {
        'all_tests': all_tests,
        'all_tests_paginator_data': all_tests_paginator_data,
        'all_category': all_category,
    }

    return render(request, template, context)

########################################################################################


def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_doctor:
                # messages.info(request, f"You are now logged in as {username}")
                return redirect('portal:doctor_home')
            else:
                return redirect('portal:patient_home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request = request,
                    template_name = "registration/login.html",)
