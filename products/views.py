from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here.
def get_index (request):
    product = Product.objects.all()
    return render( request, "products/index.html", {'product': product})
    
def create_post(request):
    if request.method=="POST":
        form = ProductsForm(request.POST, request.FILES)
        product = form.save(commit=False)
        product.save()
        return redirect("products")
    else:
        form = ProductsForm()
    items = ProductsForm()
    return render(request, "products/create_item.html", { 'form': form, 'items': items})

