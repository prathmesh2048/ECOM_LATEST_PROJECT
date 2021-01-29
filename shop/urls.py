from django.urls import path, include
from .views import index, detail, cartHandler

urlpatterns = [
 
    path('', index, name='index'),
    path('products/<slug:slug_name>',detail,name='detail'),
    path('cartHandler', cartHandler, name='cartHandler'),
]