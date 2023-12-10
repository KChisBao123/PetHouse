from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
]