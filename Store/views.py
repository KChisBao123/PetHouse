from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer, Cart, Product, CartItems

# Create your views here.
def Store(request):
    # if request.user.is_authenticated:
    #     # customer = request.user.customer
    #     # cart, created = Cart.objects.get_or_create(Customer = Customer, completed = False)
    #     # cartItems = Cart.cartItems_set_all()
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    pageNumber = request.GET.get('page')
    try:
        products = paginator.page(pageNumber)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'store.html', {'products': products})

def Cart(request):
    return render(request, 'cart.html')

def Checkout(request):
    return render(request, 'checkout.html')

@csrf_protect
def SignUp(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'signup.html', {'form': form})