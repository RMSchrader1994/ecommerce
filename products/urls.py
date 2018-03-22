from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from .views import *


urlpatterns = [
	url(r'^$', get_index, name="products"),
	url(r'^create$', create_post, name="create_post"),
	url(r'item/(\d+)$', product_item, name='product_item'),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]