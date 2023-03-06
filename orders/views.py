
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from basket.basket import Basket
from django.urls import reverse

from customerportal.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Order, OrderItem

def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':

        # order_key = request.POST.get('order_key') # to confirm the order
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        # Check if order exists
        order = Order.objects.create(user_id=user_id, table_number='name', total_bill=baskettotal)
        order_id = order.pk

        for item in basket: #orderItem createion
            OrderItem.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

        redirect_url = reverse("customerportal:all_products")

        response = JsonResponse({
            'success': 'Return something',
            'url':redirect_url
            })

        basket.clear()

        return response

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
