from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models import Product
from store.models import Order


# login get method
class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.POST.get('customer')
        cart = request.POST.get('cart')
        for product in products:
            order = Order(customer = Customer(id=customer),
                          product= product,
                          price = product.price,
                          address = address,
                          phone= phone,
                          quantity = cart.get(str(product.id)))
            order.save()
        request.session['cart']= {}
        return redirect('cart')