from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('products/', productsView, name='products'),
    path('product/<int:id>', product, name='product'),
]