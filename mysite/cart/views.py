from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Shop
from django.views.decorators.http import require_POST
from cloudipsp import Api, Checkout


def buy(request):
    cart = Cart(request)
    total = int(cart.get_total_price())
    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "KZT",
        "amount": str(total)+'00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Shop, id=product_id)
    form = CartAddProductForm(request.POST)
    print(form['quantity'])
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    else:
        print(form.errors)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Shop, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
