"""Flightmode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
# from custom_users import urls 
# from .views import home
# from .views import DevelopersView

urlpatterns = [
    path('admin/', admin.site.urls),
    # App1 (diagnostic_centers)
    path('',include('Custom_users.urls')),
    # App2 (diagnostic_centers)
    path('',include('Doctor_user.urls')),
    # App3 (diagnostic_centers)
    path('', include('diagnostic_centers.urls', namespace='diagnostic_centers')),

    # App4 (tests)
    path('', include('tests.urls', namespace='tests')),

    # App4 (report_processing)
    path('', include('report_processing.urls', namespace='report_processing')),

    # Allauth (built-in)
    # path('accounts/', include('allauth.urls')),

    # # Developers
    # path('developers/', DevelopersView.as_view(), name='developers'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
