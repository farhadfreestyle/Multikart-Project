from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from core.forms import Subscribe
from django.template.defaulttags import register
from product.models import Product
from order.forms import Billing
from order.models import Checkout
from order.models import Order, Cart
from product.models import P_Image
from django.http import JsonResponse
import json
from .utils import cookieCart, cartData, guestOrder
from django.core.exceptions import ValidationError



def cart(request):
    @register.filter
    def product_images(product, index):
        return P_Image.objects.all().filter(product=product)[index].image.url
    data = cartData(request)
    cart = data['cart']
    order = data['order']
    products = data['product']
    print(products)
    context = {'products': products, 'order': order, 'cart': cart}
    return render(request, 'order/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user, complete=False)

    cart, created = Cart.objects.get_or_create(order=order, product=product)

    if action == 'add':
        cart.quantity = (cart.quantity + 1)
    elif action == 'remove':
        cart.quantity = (cart.quantity - 1)
    cart.user = user
    cart.save()

    if cart.quantity <= 0:
        cart.delete()

    return JsonResponse('Item was added', safe=False)


def checkout(request):
    data = cartData(request)
    cart = data['cart']
    order = data['order']
    product = data['product']
    context = {
        'forms': Billing,
        'product': product,
        'order': order,
        'cartItems': cart
    }

    if request.method == 'POST':
        form = Billing(request.POST)
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.first_name = form.cleaned_data['first_name']
            checkout.last_name = form.cleaned_data['last_name']
            checkout.phone = form.cleaned_data['phone']
            checkout.email = form.cleaned_data['email']
            checkout.country = form.cleaned_data['country']
            checkout.address = form.cleaned_data['address']
            checkout.town = form.cleaned_data['town']
            checkout.state = form.cleaned_data['state']
            checkout.postal_code = form.cleaned_data['postal_code']
            checkout.shipping = form.cleaned_data['shipping']
            checkout.payment = form.cleaned_data['payment']
            checkout.save()
         
            return redirect('order:order')
        else:
            raise ValidationError('There is a problem')



    return render(request, 'order/checkout.html', context)



def order(request):
    return render(request, 'order/order-success.html', )


def vendor(request):
    return render(request, 'order/vendor-profile.html', )