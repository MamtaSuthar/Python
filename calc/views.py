from django.shortcuts import render, redirect
from .models import Member
from django.contrib import messages
from random import randint, randrange
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.user.is_authenticated:
       rest = Member.objects.all().values()
       return render(request,'index.html',{'rest':rest})
    elif 'vendor_user' in request.session:
      rest = Member.objects.filter(user_id=request.session['vendor_user']['id'],is_vendor=1).values()
      return render(request,'index.html',{'rest':rest})
    else:
       rest = Member.objects.all().values()
       return render(request,'index.html',{'rest':rest})

def addmembers(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        location = request.POST['location']
        state = request.POST['state']
        city = request.POST['city']
        img = request.FILES.get('img')
        user_id = request.session['vendor_user']['id']
        is_vendor = 1
   
        if 'offer' in request.POST:
            offer = 1
        else:
            offer = 0

        new_member = Member(
            name=name,
            price=price,
            offer=offer,
            location=location,
            state=state,
            city=city,
            user_id=user_id,
            img = img,
            is_vendor=is_vendor,
        )

        if new_member:
            new_member.save()
            messages.success(request, 'Vendor Member Added Successfully!')
            return render(request, 'vendors/addmembers.html')
        else:
            messages.error(request, 'Failed to add Vendor Member')
            return render(request, 'vendors/addmembers.html')
    else:
        return render(request, 'vendors/addmembers.html')

def members(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'vendors/member.html', {'member': member})

def view_members(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'users/view_members.html', {'member': member})