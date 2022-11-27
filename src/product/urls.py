import imp
from django.urls import path
from . import views
from product import views

app_name = 'products'


app_name = 'product'
urlpatterns = [
    path('category-page/', views.category, name='category-page'),
    path('product-page/<slug:slug>/', views.product_detail, name='product_details'),
    path('search/', views.search, name = 'search')


]