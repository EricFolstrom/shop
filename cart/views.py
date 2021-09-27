from django.shortcuts import render, get_object_or_404
from .models import Cart
from products.models import Product


def cart(request):

    cart = Cart.objects.all()
    cart_count = len(cart)
    context = []

    for cart_item in cart:
        try:
            product = get_object_or_404(Product, pk=cart_item.product_id)
            new_cart_item = {
                'product_id': product.id,
                'title': product.title
            }
            context.append(new_cart_item)
        except:
            pass

    return render(request, 'cart/index.html', {'cart': context, 'cart_count': cart_count})
