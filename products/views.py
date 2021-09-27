from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.models import Cart


def index(request):
    cart = Cart.objects.all()
    cart_count = len(cart)
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products, 'cart_count': cart_count})


def details(request, id):
    cart = Cart.objects.all()
    cart_count = len(cart)
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/details.html', {'product': product, 'cart_count': cart_count})


def base(request):
    cart = Cart.objects.all()
    cart_count = len(cart)
    return render(request, 'products/base.html', {'cart': cart, 'cart_count': cart_count})
