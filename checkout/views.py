from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import *
from decimal import Decimal
from cart.utils import get_cart_items
from django.utils import timezone
from .models import OrderLineItem
from django.conf import settings


# Create your views here.
def checkout(request):

    if request.method=="POST":
        
        order_form = OrderForm(request.POST)
        order = order_form.save(commit=False)
        order.date = timezone.now()
        
        order.save()
        
        cart = request.session.get('cart', {})
        for id, quantity in cart.items():
            product = get_object_or_404(Product, pk=id)
            order_line_item = OrderLineItem (
                order = order,
                product = product,
                quantity = quantity
                )
            order_line_item.save()
        
        
        
        del request.session['cart']
        return redirect("home")
    
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY }
        
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items(cart)
        
        context.update(cart_items_and_total)
    
    return render(request, "checkout/checkout.html", context)