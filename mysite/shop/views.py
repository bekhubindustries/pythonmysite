from django.shortcuts import render, HttpResponse, redirect
from .models import *
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from .models import Shop


def index(request):
    items = Shop.objects.all().order_by('price')

    return render(request, 'shop/index.html', {'items': items})


def about(request):
    return HttpResponse(request, 'shop/about.html')


def detail(request, item_id):
    try:
        item: object = Shop.objects.get(id=item_id)
        cart_product_form = CartAddProductForm()
    except:
        return redirect(index, permanent=True)

    return render(request, 'shop/detail.html', {'item': item, 'cart_product_form': cart_product_form})


def just(request):
    # Ваша логика обработки запроса
    return render(request, 'Shop/my_template.html')
