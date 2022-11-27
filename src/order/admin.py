from django.contrib import admin
from order.models import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.
class CartModelAdmin(admin.ModelAdmin):
    list_display = [ 'product', 'quantity', 'date_added', 'order']
    search_fields = [ 'product', 'quantity', 'date_added', 'order']


class VendorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'rating', 'followers', 'reviews', 'facebook', 'instagram',
                    'twitter', 'gmail']
    search_fields = ['name', 'image', 'description', 'rating', 'followers', 'reviews', 'facebook', 'instagram',
                     'twitter', 'gmail']


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_ordered', 'complete', 'transaction_id']
    search_fields = ['user', 'date_ordered', 'complete', 'transaction_id']


class CheckoutModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'town', 'state', 'postal_code', 'shipping', 'payment', ]
    search_fields = ['user', 'order', 'town', 'state', 'postal_code', 'shipping', 'payment', ]




# Register your models here.
admin.site.register(Cart, CartModelAdmin)
admin.site.register(Vendor_Profile, VendorModelAdmin)
admin.site.register(Checkout, CheckoutModelAdmin)
admin.site.register(Order, OrderModelAdmin)