from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.contrib.auth.models import User 
# from .models import User
# from .forms import UserForm
import logging

def home(request):
    rest = Member.objects.all().values()
    return render(request,'index.html',{'rest':rest})

