from math import prod
from os import name
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.core.exceptions import ValidationError
from product.forms import *
from product.models import *
from django.template.defaulttags import register
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from product.serializers import ProductSerializer, CategorySerializer
from product.models import Product
from order.utils import cookieCart, cartData
from django.core.paginator import Paginator
from django.db.models import Min, Max





# def category(request):
#     products = Product.objects.all().order_by('-id')
#     sorted_products = Product.objects.all().order_by('-id')
#
#     brands = Brand.objects.all()
#     product_images = {}
#     product_ids = []
#     for each_product in products:
#         product_images[each_product.id] = P_Image.objects.filter(product=each_product.id)
#         product_ids.append(each_product.id)
#
#     @register.filter
#     def get_range(value):
#         return range(12, value + 1)
#
#     @register.filter
#     def get_index(list, value):
#         return list[value]
#
#     @register.filter
#     def get_value(item):
#         return item.image.url
#
#     @register.filter
#     def get_product(item, value):
#         for each in item:
#             if each == products[value].id:
#                 return item[each][0]
#
#     context_data = {
#         'products': products,
#         'brands': brands,
#         'product_images': product_images,
#         'product_ids': product_ids,
#         'sorted_products': sorted_products
#
#     }
#
#     return render(request, 'product/category-page.html', context=context_data)


def category(request):
    @register.filter
    def product_images(product, index):
        return P_Image.objects.all().filter(product=product)[index].image.url
    p = Paginator(Product.objects.all(), 6)

    products = Product.objects.all()
    sizes = Size.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    colors = Color.objects.all()
    product_list_1 = Product.objects.all().order_by('-id')[0:3]
    product_list_2 = Product.objects.all().order_by('-id')[3:6]
    color_id = request.GET.get('color')
    size_id = request.GET.get('size')
    brand_id = request.GET.get('brand')
    price = request.GET.get('price')
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    if color_id:
        p = Paginator(Product.objects.filter(color=color_id), 6)
    if size_id:
        p = Paginator(Product.objects.filter(size=size_id), 6)
    if brand_id:
        p = Paginator(Product.objects.filter(brand=brand_id), 6)
    if price:
        int_price = int(price)
        p = Paginator(Product.objects.filter(price__lte=int_price), 6)
    page = request.GET.get('page')
    products_list = p.get_page(page)
    context = {'products': products,
               'sizes': sizes,
               'brands': brands,
               'colors': colors,
               'categories': categories,
               'min_price': min_price,
               'max_price': max_price,
               'product_list1': product_list_1,
               'product_list2': product_list_2,
               'products_list': products_list,

               }

    return render(request, 'product/category-page.html', context)


def product_detail(request: HttpRequest, slug) -> HttpResponse:
    @register.filter
    def product_images(product, index):
        return P_Image.objects.all().filter(product=product)[index].image.url
    product = Product.objects.filter(slug=slug).first()
    all_products = Product.objects.all()
    product_list_1 = Product.objects.all().order_by('-id')[0:3]
    product_list_2 = Product.objects.all().order_by('-id')[3:6]
    context = {
        'product': product,
        'forms': WriteReviewForm,
        'all_products':all_products,
        'product_list1':product_list_1,
        'product_list2':product_list_2,

    }
    if request.method == 'POST':
        form = WriteReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.name = form.cleaned_data['name']
            review.email = form.cleaned_data['email']
            review.review_title = form.cleaned_data['review_title']
            review.review_desc = form.cleaned_data['review_desc']
            review.product = product
            review.save()
        else:
            raise ValidationError
        
       

    return render(request, 'product/product-page.html', context)


def search(request):
    products = Product.objects.all().order_by('-id')

    brands = Brand.objects.all()
    product_images = {}
    product_ids = []
    for each_product in products:
        product_images[each_product.id] = P_Image.objects.filter(product=each_product.id)
        product_ids.append(each_product.id)

    @register.filter
    def product_images(product, index):
        return P_Image.objects.all().filter(product=product)[index].image.url

    data = {
        'form': Search,

    }
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            input = form.cleaned_data['input']
            found_products = [i for i in Product.objects.filter(name__icontains=input)]
            data['found_products'] = found_products


        else:
            raise ValidationError

    return render(request, 'product/search.html', context=data)


# def product(request, id):
#     products = Product.objects.all()
#     sorted_products = Product.objects.all().order_by('-id')
#     product_images = {}
#     for each_product in sorted_products:
#         product_images[each_product.id] = P_Image.objects.filter(product=each_product.id)
#
#     sorted_product_images = {}
#     for each_product in products:
#         sorted_product_images[each_product.id] = P_Image.objects.filter(product=each_product.id)
#
#     @register.filter
#     def get_value(item):
#         return item.image.url
#
#     @register.filter
#     def get_product(item, value):
#         for each in item:
#             if each == sorted_products[value].id:
#                 return item[each][0]
#
#     @register.filter
#     def make_number(number, discount):
#         return round(number / (discount / 100), 2)
#
#     @register.filter
#     def get_pk_category(number):
#         return Product.objects.get(id=number).category.all()[0]
#
#     @register.filter
#     def get_product_category(product):
#         return product.category.all()[0]
#
#     @register.filter
#     def get_image(item, value):
#         for each in product_images:
#             if item.id == each:
#                 return product_images[each][value].image.url
#
#     @register.filter
#     def all_size(product):
#         return product.size.all()
#
#     data = {'forms': WriteReviewForm,
#             'products': products,
#             'pk': id,
#             'sorted_product_images': sorted_product_images,
#             'sorted_products': sorted_products
#
#             }
#     if request.method == 'POST':
#         form = WriteReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             raise ValidationError
#     return render(request, 'product/product-page.html', context=data, )


###CRUD###

class ListProductAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductAPIView(CreateAPIView):
    """This endpoint allows for creation of a product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific product by passing in the id of the product to update"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific product from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveProductAPIView(RetrieveAPIView):
    """This endpoint list all of the available products from the database"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


###CRUD###


class Createview(CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


from django.shortcuts import get_object_or_404


class Updateview(UpdateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'


class Deleteview(DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'


class Listview(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
