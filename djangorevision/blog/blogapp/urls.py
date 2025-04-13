"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .import views

urlpatterns = [
    path("forms",views.forms),
    path("post",views.index),
    path("show",views.show ,name='show'),
    path("",views.registerpg),
    path("registerview",views.registerview),
    path("forms",views.forms),
    path("edit/<str:pk>",views.updateData, name='updateData'),
    path("delete/<id>",views.deleteData, name='deleteData'),
    path("check",views.check),
    path("login",views.loginpg,name="login"),
    path("logout",views.logoutuser,name='logout'),
    
]
