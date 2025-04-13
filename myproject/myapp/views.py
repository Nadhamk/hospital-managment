
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import *
from . forms import *




def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
  
def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect("contact")  # Redirect to clear the form after submission
            
    form=ContactForm
    context={
        'form':form
        }
    return render(request,"contact.html",context)  

def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking successful!")
            return redirect("booking")  # Redirect to clear form
    
    form=BookingForm
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)

    
def doctor(request):
    dict_doc={
        'doctors':Doctor.objects.all()
    }
    return render(request,"doctor.html",dict_doc)
    
    

def department(request):
    dict_dep={
        'dept':Department.objects.all()
    }
    return render(request,"department.html",dict_dep)

