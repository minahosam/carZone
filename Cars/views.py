from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.
def carsPage(request):
    newest_car = cars.objects.order_by('-created_date')
    print('1')
    page = request.GET.get('page')
    print('1')
    paginator = Paginator(newest_car, 2)
    print('1')
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
    return render(request, 'Pages/cars.html',{'car': pages})

def carDetailsPage(request,slug):
    car=cars.objects.get(slug=slug)
    return render(request, 'Pages/carDetails.html',{'car':car})

def searchPage(request):
    keyword = request.GET.get('keyword',False)
    model = request.GET.get('model',False)
    year = request.GET.get('year',False)
    location = request.GET.get('location',False)
    body = request.GET.get('body',False)
    min_price = request.GET.get('min_price',False)
    max_price = request.GET.get('max_price',False)
    sarched_car = None
    if keyword:
        sarched_car = cars.objects.filter(Q(description__icontains=keyword) & Q(car_title__icontains=keyword))
    print(sarched_car)
    filtered_car = None
    if model or year or location or body or min_price or max_price:
        filtered_car = cars.objects.filter(Q(model__icontains=model) | Q(year__icontains=year) | Q(city__icontains=location) | Q(body_style__icontains=body) | Q(price__lte=min_price) | Q(price__gte=max_price))
    print(filtered_car)
    print(model , year, location, body, min_price, max_price)
    return render(request, 'Pages/search.html',{'cars':sarched_car,'filter_car':filtered_car})