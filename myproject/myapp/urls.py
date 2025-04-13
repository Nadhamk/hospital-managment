from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('booking/', views.booking, name="booking"),
    path('doctor/', views.doctor, name="doctor"),
    path('department/', views.department, name="department"),
]
