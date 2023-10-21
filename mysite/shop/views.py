from django.shortcuts import render, HttpResponse, redirect
from .models import *


# from cart.forms import CartAddProductForm
# from django.http import HttpResponse


def index(request):
    items = Shop.objects.all()
    return render(request, 'shop/index.html', {'items': items})


def about(request):
    return render(request, 'shop/about.html')


def detail(request, item_id):
    try:
        item: object = Shop.objects.get(id=item_id)
        cart_product_form = CartAadProductForm()
    except:
        return redirect(index, permanent=True)
    return render(request, 'shop/index.html', {'item': item, 'cart_product_form': cart_product_form})
