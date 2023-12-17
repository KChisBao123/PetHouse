from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    nphone = models.TextField(max_length=11)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid5, unique=True, editable=False)
    completed = models.BooleanField(default=False)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=10.55)
    description = models.TextField()
    image = models.ImageField()

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)