"""goal3 URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path

#connecting incident_create to usersapp
from .views import home, incident_create, responder, search_responses, aboutus

# helps with video upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('incident/create/', incident_create, name='incident_create'),
    path('responder', responder, name='responder'),
    path('search/responses/', search_responses, name='search_responses'),
    path('aboutus', aboutus, name='aboutus')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
