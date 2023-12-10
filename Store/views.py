from django.shortcuts import render
from django.http import Http404

# Create your views here.
def Store(request):
    return render(request, 'store.html')
def Cart(request):
    return render(request, 'cart.html')
def Checkout(request):
    return render(request, 'checkout.html')