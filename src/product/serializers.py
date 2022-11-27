from rest_framework import serializers
from product.models import Category
from product.models import Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"