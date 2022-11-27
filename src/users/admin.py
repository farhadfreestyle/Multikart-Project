from django.contrib import admin
from users.models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'password', 'phone', 'message', 'flat', 'address', 'zipcode', 'country', 'city', 'region','is_active', 'staff', 'admin']
    search_fields = ['id', 'first_name', 'last_name', 'email', 'password', 'phone', 'message', 'flat', 'address', 'zipcode', 'country', 'city', 'region','is_active', 'staff', 'admin']
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['image', 'product_id', 'user_id']
    search_fields = ['image', 'product_id', 'user_id']
# Register your models here.


admin.site.register(User, UserModelAdmin)
admin.site.register(Wishlist, WishlistModelAdmin)