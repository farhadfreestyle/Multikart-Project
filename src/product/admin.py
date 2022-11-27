from django.contrib import admin
from product.models import *
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'email', 'review_title', 'review_desc', 'product']
    search_fields = ['name', 'rating', 'email', 'review_title', 'review_desc', 'product']


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'discount_percent', 'title', 'availablity', 'rating', 'status',
                    'description', 'fabric', 'material', 'video', 'quantity', 'created_at', 'digital', 'slug']
    search_fields = ['id', 'name', 'price', 'discount_percent', 'title', 'availablity', 'rating', 'status',
                     'description', 'fabric', 'material', 'video', 'quantity', 'created_at', 'digital', 'slug']


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category']
    search_fields = ['category']


class PImageModelAdmin(admin.ModelAdmin):
    list_display = ['image_name', 'image', 'product']
    search_fields = ['image_name', 'image', 'product']


class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'brand_logo']
    search_fields = ['brand', 'brand_logo']


class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['color']
    search_fields = ['color']


class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']


class SaleModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'enddate']
    search_fields = ['product', 'amount', 'enddate']



# Register your models here.
admin.site.register(WriteReview, ReviewModelAdmin)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(Category, CategoryModelAdmin)
admin.site.register(P_Image, PImageModelAdmin)
admin.site.register(Brand, BrandModelAdmin)
admin.site.register(Color, ColorModelAdmin)
admin.site.register(Size, SizeModelAdmin)
admin.site.register(Sale, SaleModelAdmin)