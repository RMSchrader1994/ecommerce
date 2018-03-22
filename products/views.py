from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import *
from reviews.forms import ReviewForm
from reviews.models import Review

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
    
def product_item(request, id):
    product = get_object_or_404(Product, pk=id)
    review = Review.objects.all()
    form = ReviewForm()
    return render(request, "products/product-item.html", {'product': product, 'review': review,'review_form': form})

