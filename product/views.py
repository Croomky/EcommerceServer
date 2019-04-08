from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import RetrieveAPIView

from .models import Product
from .serializers import ProductDetailsSerializer

class ProductDetails(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_url_kwarg = 'id'
