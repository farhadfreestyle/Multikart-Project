import imp
from django.urls import path
from order import views

app_name = 'order'
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', views.order, name = 'order'),
    path('vendor/', views.vendor),
    path('update_item/', views.updateItem, name="checkout")

]