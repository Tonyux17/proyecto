# views.py

from django.shortcuts import render
from .models import Product

def landing_page(request):
    products = Product.objects.all()
    return render(request, 'landing/landing_page.html', {'products': products})
