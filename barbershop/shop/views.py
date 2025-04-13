from django.shortcuts import render, get_object_or_404
from .models import Product

def shop_home(request):
    return render(request, 'shop/home.html')

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def cart_view(request):
    return render(request, 'shop/cart/detail.html')

def checkout_view(request):
    return render(request, 'shop/checkout.html')
