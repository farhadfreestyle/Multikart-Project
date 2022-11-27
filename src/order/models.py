from django.db import models
from users.models import User
from datetime import datetime


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.UUIDField

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        cart = self.cart_set.all()
        total = sum([product.get_total for product in cart])
        return total

    @property
    def get_cart_items(self):
        cart = self.cart_set.all()
        total = sum([product.quantity for product in cart])
        return total

    @property
    def shipping(self):
        shipping = False
        cart = self.cart_set.all()
        for i in cart:
            if i.product.digital == False:
                shipping = True
        return shipping


#####################################################################
class Cart(models.Model):
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(default=datetime.now)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = verbose_name

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


###################################################################################
class Vendor_Profile(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    description = models.TextField()
    rating = models.FloatField()
    followers = models.IntegerField()
    reviews = models.TextField()
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Vendor_Profile'
        verbose_name_plural = verbose_name


CHECK = 1
CASH = 2
PAYPAL = 3
choices3 = ((CHECK, "Check Payment"), (CASH, "Cash On Delivery"), (PAYPAL, "PayPal"))


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    town = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    shipping = models.CharField(max_length=30)
    payment = models.CharField(max_length=30, choices=choices3,
                               default=CHECK)

    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = verbose_name