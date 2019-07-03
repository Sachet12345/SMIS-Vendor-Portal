from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Items

def login(request):
    count=1
    return render(request, 'vendor_portal/login.html') 

def logout(request):
    count=0
    return render(request, "vendor_portal/login.html")


def portal(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                request.session['username']=username
                return render(request, 'vendor_portal/portal.html')
            else:
                message="Your account was inactive."
                return render(request, "vendor_portal/login.html",{"messg":message})
        else:
            message="Invalid credentials"
            return render(request, "vendor_portal/login.html",{"messg":message})
    else:
        return render(request, 'vendor_portal/login.html', {})

def add(request):
    if request.method == 'POST':
        if request.POST.get('catNo') and request.POST.get('itemName'):
            item=Items()
            item.catNo= request.POST.get('catNo')
            item.itemName= request.POST.get('itemName')
            item.quantity= request.POST.get('quantity')
            item.price= request.POST.get('price')
            item.description= request.POST.get('description')
            item.vendorName= request.session.get('username')
            item.save()
                
            return render(request, 'vendor_portal/portal.html')  
    
    return render(request,'vendor_portal/portal.html')
