from decimal import Decimal
from django.conf import settings
from shop.models import Shop


class Cart(object):
    def __init__(self, request):
        # Иниццализация корзины
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем пустую корзину если не было предыдущей сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        # Перебираем товары в корзине и получаем их из базы данных
        product_ids = self.cart.keys()
        # получаем товары и добавляе их в корзину
        products = Shop.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['quantity'] * item['price']
            yield item

    def __len__(self):
        # количество товаров в корзине
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        # Очищаем сесси.
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        # Сохраняем товар
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False, ):
        # добавляем товар в корзину и обновляем его количество
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        # Удаление товара
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        # Получаем общую сумму
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
