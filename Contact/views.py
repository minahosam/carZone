from django.shortcuts import render,redirect
from django.urls import reverse
from .models import *
from Cars.models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        message_title = request.POST.get('customer_need')
        car_title =request.POST.get('car_title')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        refuse_ = contact.objects.filter(first_name=first_name)
        refuse__ = contact.objects.filter(email=email)
        if refuse_ | refuse__:
            messages.error(request,'you have already make inquiry about this car')
            return redirect('cars:cars')
        req_car = cars.objects.get(car_title=car_title)
        send_mail(
                    message_title,
                    message,
                    email,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
        con = contact.objects.create(first_name=first_name, last_name=last_name,message_title=message_title,city=city,state=state,email=email,phone=phone,car_title=req_car,message=message,user_id=user_id,car_id=req_car.id)
        con.save()
        messages.success(request,'your request has been submitted')
        return redirect(reverse('cars:carDetails',kwargs={'slug':req_car.slug}))