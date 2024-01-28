from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) 
    password = models.CharField(max_length=255) 
    phone = models.CharField(max_length=12) 
    last_login = models.DateTimeField(auto_now=True)  
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)  

    
class Meta:
        app_label = 'accounts'