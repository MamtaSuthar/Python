from django.shortcuts import render, redirect
import logging
from django.contrib.auth.models import User 
from datetime import date
from random import randint, randrange
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password
from .models import Vendor
from .middleware.custommiddleware import VendorAuthenticationMiddleware

def user_register(request):
     return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = f'user_{randrange(1000000)}'
        email      = request.POST['email']
        password   = request.POST['password']
        is_staff   = 0
        is_active  = 1
        date_joined   = date.today()


        if User.objects.filter(email=email).exists():
            messages.info(request, 'User is already exists !')
            return render(request, 'register.html', {'error_message': 'User already exists'})
        else:
            User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email, password=password,is_staff=is_staff, is_active=is_active,date_joined=date_joined)
            messages.info(request, 'User created successfully !')
            return render(request, 'index.html')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
  
        user = authenticate(request, username = username, password = password)
   
        if user is not None:
            auth_login(request, user) 
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('register')

    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def editusers(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email_feild = request.POST['email']
        password_feild = make_password(request.POST['password'])

        User.objects.filter(email=email_feild).update(first_name=fname,last_name=lname,email=email_feild,password=password_feild)
        return render(request, 'editusers.html')
    else:
        return render(request, 'editusers.html')
    
def vendor(request):
     return render(request, 'vendor_register.html')

def vendor_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email      = request.POST['email']
        password   = make_password(request.POST['password'])
        phone   = request.POST['phone']
        is_active  = 1
        date_joined   = date.today()

        if Vendor.objects.filter(email=email).exists():
            messages.info(request, 'Vendor is already exists !')
            return render(request, 'register.html', {'error_message': 'Vendor already exists'})
        else:
            new_vendor = Vendor(
                name=name,
                email=email,
                password=password,
                phone=phone,
                is_active=is_active,
                date_joined=date_joined
            )
            new_vendor.save() 

            # Log the vendor in
            middleware_instance = VendorAuthenticationMiddleware()
            authenticated_vendor = middleware_instance.authenticate_vendor(request, email, password)

            if authenticated_vendor:
                messages.success(request, 'Vendor created and logged in successfully!')
                return render(request, 'index.html')
            else:
                messages.error(request, 'Failed to authenticate vendor')
                return render(request, 'vendor_register.html')
    else:
        return render(request, 'vendor_register.html')

def vendor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = make_password(request.POST['password'])
    
       # Log the vendor in
        middleware_instance = VendorAuthenticationMiddleware()
        authenticated_vendor = middleware_instance.authenticate_vendor(request, email, password)

        if authenticated_vendor:
            messages.success(request, 'Vendor logged in successfully!')
            return render(request, 'vendor_index.html')
        else:
            messages.error(request, 'Failed to authenticate vendor')
            return render(request, 'vendor_register.html')

    else:
        return render(request, 'vendor_register.html')
    

