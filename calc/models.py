from django.db import models

class Member(models.Model):
    name     = models.CharField(max_length=255)
    img      = models.ImageField(upload_to='pics')
    price    = models.CharField(max_length=255)
    offer    = models.BooleanField(default = False)
    location = models.CharField(max_length=255)
    
class Meta:
        app_label = 'calc'
