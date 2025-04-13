from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.TextField()
    pub_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Data(models.Model):
    name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Login(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    type=models.IntegerField()
    
    def __str__(self):
        return self.username