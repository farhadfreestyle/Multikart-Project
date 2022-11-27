import json
from product.models import *
from order.models import *


def cookieCart(request):
    # Create empty cart for now for non-logged in user
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        print('CART:', cart)

    product = []
    order = {'get_cart_total': 0, 'get_cart_product': 0, 'shipping': False}
    cart = order['get_cart_product']

    for i in cart:
        # We use try block to prevent product in cart that may have been removed from causing error
        try:
            if (cart[i]['quantity'] > 0):  # product with negative quantity = lot of freebies
                cart += cart[i]['quantity']

                product = Product.objects.get(id=i)
                total = (product.price * cart[i]['quantity'])

                order['get_cart_total'] += total
                order['get_cart_product'] += cart[i]['quantity']

                item = {
                    'id': product.id,
                    'product': {'id': product.id, 'name': product.name, 'price': product.price,
                                'imageURL': product.imageURL}, 'quantity': cart[i]['quantity'],
                    'digital': product.digital, 'get_total': total,
                }
                product.append(item)

                if product.digital == False:
                    order['shipping'] = True
        except:
            pass

    return {'cart': cart, 'order': order, 'product': product}


def cartData(request):
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        product = order.cart_set.all()
        cart = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cart = cookieData['cart']
        order = cookieData['order']
        product = cookieData['product']

    return {'cart': cart, 'order': order, 'product': product}


def guestOrder(request, data):
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    product = cookieData['product']

    user, created = User.objects.get_or_create(
        email=email,
    )
    user.name = name
    user.save()

    order = Order.objects.create(
        user=user,
        complete=False,
    )

    for item in product:
        product = Product.objects.get(id=item['id'])
        order = Cart.objects.create(
            product=product,
            order=order,
            quantity=(item['quantity'] if item['quantity'] > 0 else -1 * item['quantity']),
        )
    return user, order