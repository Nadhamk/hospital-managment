from django import forms
from . models import *


class DateInput(forms.DateInput):
    input_type='date'
    

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
        
        widgets={
            'booking_date':
                DateInput()
        }
        labels= {
            'p_name':"Patient Nane:",
            'p_phone':"Patient Phone Number:",
            'p_email':"Patient EmailId:",
            'doc_name':"Doctor Name:",
            'booking_date':"Booking date:"
        }
        
class ContactForm(forms.ModelForm): 
    class Meta:
        model = Contact
        fields = '__all__'
        
        labels = {
            'c_name':"Name:",
            'c_email':" Email:",
            'c_description':"Description:",
            
        }
        