from django.urls import path
from . import views

urlpatterns = [
    path('', views.Store),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('signup/', views.SignUp, name='signup'),
    path('updatecart', views.updateCart, name = 'updatecart'),
]