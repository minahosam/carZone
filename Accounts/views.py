from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from Contact.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            messages.success(request,'login successful')
            return redirect('account:dashboard')
        else:
            messages.error(request,'login failed')
            return redirect('account:login')
    else:
        return render(request, 'account/login.html')

def registerPage(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username was existed')
                return redirect('account:register')
               
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email was existed')
                    return redirect('account:register')
                else:
                    user = User.objects.create(username=username, email=email,first_name=first_name,last_name=last_name,password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request,'you are now logged in')
                    return redirect('account:dashboard')
        else:
            messages.error(request,'Password and confirm password does not match')
            return redirect('account:register')
    else:
        return render(request, 'account/register.html')

def logoutPage(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'you are now logged out')
        return redirect('/')
    return redirect('/')

@login_required(login_url='/profile/login/')
def dashboardPage(request):
    email = User.objects.get(username=request.user)
    print(email)
    inquire_message = contact.objects.filter(email=email.email).order_by('-created_at')
    return render(request, 'account/dashboard.html',{'inquire_message':inquire_message})