from django.contrib.auth.models import User, Group
from rest_framework import serializers, generics
from product.models import Product
from product.models import Category
from order.models import Cart


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'quantity', 'date_added', 'order', 'product')

        depth = 1


