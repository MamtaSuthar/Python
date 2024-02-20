from django.shortcuts import render, redirect
from .models import Member
from django.contrib.auth.models import User 
from accounts.models import Vendor
from django.contrib import messages
from random import randint, randrange
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'GET':
        query_name = request.GET.get('name')
        query_location = request.GET.get('location')

        if request.user.is_authenticated:
            queryset = Member.objects.all()
        elif 'vendor_user' in request.session:
            queryset = Member.objects.filter(user_id=request.session['vendor_user']['id'], is_vendor=1)
        else:
            queryset = Member.objects.all()

        if query_name:
            queryset = queryset.filter(name__icontains=query_name)
        if query_location:
            queryset = queryset.filter(location__icontains=query_location)

        rest = queryset.values()
        return render(request, 'index.html', {'rest': rest})
   
    
def addmembers(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        location = request.POST['location']
        state = request.POST['state']
        city = request.POST['city']
        desc = request.POST['desc']
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
            desc= desc,
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
    if request.method == 'POST':
        try:
            member = Member.objects.get(pk=id)
            member.name = request.POST['name']
            member.price = request.POST['price']
            member.location = request.POST['location']
            member.state = request.POST['state']
            member.city = request.POST['city']
            member.desc = request.POST['desc']
            member.img = request.FILES.get('img')
            user_id = request.session['vendor_user']['id']
            
            # Update user if it exists
            if Vendor.objects.filter(pk=user_id).exists():
                member.user_id = user_id
            else:
                # Handle case where user doesn't exist or session is not set properly
                raise ValueError('User not found or session not properly set.')

            if 'offer' in request.POST:
                member.offer = 1
            else:
                member.offer = 0

            member.save()
            messages.success(request, 'Vendor Member Updated Successfully!')
            return render(request, 'vendors/member.html', {'member': member})
        except Member.DoesNotExist:
            messages.error(request, 'Member not found')
            return render(request, 'vendors/member.html', {'member': member})
        except Exception as e:
            messages.error(request, f'Failed to update vendor member: {str(e)}')
            return render(request, 'vendors/member.html', {'member': member})
    else:
        member = Member.objects.get(pk=id)
        return render(request, 'vendors/member.html', {'member': member})

def view_members(request, id):
    member = Member.objects.get(pk=id)
    return render(request, 'users/view_members.html', {'member': member})