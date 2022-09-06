from operator import sub
from django.shortcuts import render,redirect
from .models import *
from Cars.models import *
from django.urls import reverse
from Contact.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def HomePage(request):
    team = TeamMember.objects.all()
    featured_cars = cars.objects.order_by('-created_date').filter(is_featured = True)
    all_cars = cars.objects.order_by('-created_date')
    model_list = cars.objects.values_list('model', flat=True).distinct()
    location_list = cars.objects.values_list('city', flat=True).distinct()
    year_list = cars.objects.values_list('year', flat=True).distinct()
    body_style = cars.objects.values_list('body_style',flat=True).distinct()
    return render(request, 'Pages/homepage.html',{'team':team,'featured_cars':featured_cars,'all_cars':all_cars,'model_list':model_list,'location_list':location_list,'year_list':year_list,'body_style':body_style})

def aboutPage(request):
    team = TeamMember.objects.all()
    return render(request, 'Pages/about.html',{'team':team})

def contactPage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        send_mail(
                    subject,
                    message,
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
        con = contact.objects.create(first_name=name, last_name=name,message_title=subject,email=email,phone=phone,message=message)
        con.save()
        messages.success(request,'your request has been submitted')
        return redirect(reverse('home:contact'))
    else:
        return render(request, 'Pages/contact.html')

def servicesPage(request):
    return render(request, 'Pages/services.html')

