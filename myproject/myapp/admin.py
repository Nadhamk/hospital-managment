from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=("id","p_name","p_phone","p_email","doc_name","booking_date")
admin.site.register(Booking,BookingAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=("c_name","c_email","c_description")
    admin.site.register(Contact)