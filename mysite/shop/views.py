from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from .models import *
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from .models import Shop
from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render


def index(request):
    items = Shop.objects.all().order_by('price')
    return render(request, 'shop/index.html', {'items': items})


def index_men(request):
    items = Shop.objects.filter(category=6).order_by('price')

    return render(request, 'shop/index.html', {'items': items})


def index_PERFUMES_AND_BODY_SKIN_CARE_PRODUCTS(request):
    items = Shop.objects.filter(category=7).order_by('price')

    return render(request, 'shop/index.html', {'items': items})


def index_women(request):
    items = Shop.objects.filter(category=5).order_by('price')

    return render(request, 'shop/index.html', {'items': items})


def about(request):
    return HttpResponse(request, 'shop/about.html')


def detail(request, item_id):
    try:
        item = Shop.objects.get(id=item_id)
        cart_product_form = CartAddProductForm()
    except Shop.DoesNotExist:
        # Обработка случая, когда товар с заданным item_id не найден
        return HttpResponse("Товар не найден")

    return render(request, 'shop/detail.html', {'item': item, 'cart_product_form': cart_product_form})


def just(request):
    # Ваша логика обработки запроса
    return render(request, 'Shop/my_template.html')


class Search(ListView):
    template_name = 'shop/index.html'
    context_object_name = 'items'  # Change context_object_name for clarity

    def get_queryset(self):
        search_query = self.request.GET.get('q', '')  # Use 'q' as the parameter name
        return Shop.objects.filter(name__icontains=search_query)


