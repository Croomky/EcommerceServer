from rest_framework import serializers
from django.http import HttpResponse

from product.models import Product, \
    Category,   \
    FeaturedProduct

class ProductDetailsSerializer(serializers.ModelSerializer):

    thumbnail = serializers.CharField(source='get_thumbnail_name')

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'thumbnail', 'body')

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

class ProductsByPhraseSerializer(serializers.ModelSerializer):

    thumbnail = serializers.CharField(source='get_thumbnail_name')

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'thumbnail', 'description')

class FeaturedProductsSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(source="get_id")
    name = serializers.CharField(source="get_name")
    thumbnail = serializers.CharField(source='get_thumbnail_name')
    price = serializers.FloatField(source="get_price")

    class Meta:
        model = FeaturedProduct
        fields = ('id', 'name', 'price', 'thumbnail')
    