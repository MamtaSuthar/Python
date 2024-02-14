from django.db import models

class Member(models.Model):
    name     = models.CharField(max_length=255)
    img      = models.ImageField(upload_to='pics')
    price    = models.CharField(max_length=255)
    offer    = models.BooleanField(default = False)
    location = models.CharField(max_length=255)
    city     = models.CharField(max_length=255)
    state    = models.CharField(max_length=255)
    user_id  = models.CharField(max_length=255)
    is_vendor= models.CharField(max_length=255)
    
class Meta:
        app_label = 'calc'
