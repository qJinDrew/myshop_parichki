from django.shortcuts import render
from .models import Product, Category


def shop(request):
    product = Product.objects.all()

    return render(request, 'shop/shop.html', {'shop': product})


def detail(request):
    category = Category.objects.all()
    return render(request, 'shop/shop.html', {'shop': category})





