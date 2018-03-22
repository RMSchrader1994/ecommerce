from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^view/$', view_cart, name='view_cart'),
    url(r'^add/$', add_to_cart, name='add_to_cart'),
    url(r'^delete/(\d+)$', delete_product, name='delete_product'),
]