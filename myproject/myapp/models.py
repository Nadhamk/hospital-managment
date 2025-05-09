from django.db import models

# Create your models here.
    
class Department(models.Model):
    dep_name=models.CharField(max_length=255)
    dep_description=models.TextField(max_length=255)
    
    def __str__(self):
        return self.dep_name
    
class Doctor(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctor')
    
    def __str__(self):
        return 'Dr.'+self.doc_name+ '- (' +self.doc_spec+ ')'
    
    
    
class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    
    
    def __str__(self):
        return f"Booking for {self.p_name} with {self.doc_name}"
    
class Contact(models.Model):
    c_name=models.CharField( max_length=100)
    c_email=models.EmailField()
    c_description=models.TextField()
    

                                  
  