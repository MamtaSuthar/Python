from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=254, unique=True)  # Change from ImageField to CharField
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)  # Change from BooleanField to CharField
    last_login = models.DateTimeField(auto_now=True)  # Add last_login field
    is_active = models.BooleanField(default=True)  # Change from CharField to BooleanField
    date_joined = models.DateTimeField(auto_now_add=True)  # Change from CharField to DateTimeField

    class Meta:
        app_label = 'accounts'
