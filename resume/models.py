from django.db import models

# Create your models here.

class Contact(models.Model): 
    name = models.CharField(max_length=100,default="") 
    password = models.CharField(max_length=50,default="") 
    phone = models.CharField(max_length=50,default="") 
    text = models.TextField(max_length=1000,default="") 

    def __str__(self): 
        return self.name