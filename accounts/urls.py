from django.urls import path
from . import views

urlpatterns = [

    # Register and Login Users
    path('', views.user_register, name='user_register'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout_view', views.logout_view, name='logout_view'),

    # Edit Users
    path('editusers', views.editusers, name='editusers'),
    
    #Vendor Login and Register
    path('vendor', views.vendor, name='vendor'),
    path('vendor_register', views.vendor_register, name='vendor_register'),
    path('vendor_login', views.vendor_login, name='vendor_login'),
    path('vendor_logout', views.vendor_logout, name='vendor_logout'),

    # Edit Vendor
    path('editvendors', views.editvendors, name='editvendors'),


]

