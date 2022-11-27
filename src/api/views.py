from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
# from api.serializer import CartSerializer
from order.models import Cart


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


#Cart elements

class ListCartAPIView(ListAPIView):
    """This endpoint list all of the available products from the database"""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer