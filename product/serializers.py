from rest_framework import serializers
from django.http import HttpResponse

from product.models import Product

class ProductDetailsSerializer(serializers.ModelSerializer):

    thumbnail = serializers.CharField(source='get_thumbnail_name')

    class Meta:
        model = Product
        fields = ('name', 'price', 'thumbnail', 'body')
