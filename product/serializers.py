from rest_framework import serializers
from product.models import Product

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'thumbnail', 'body')