from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from product.models import Product

class ProductDetails(RetrieveAPIView):
    # queryset = Product.find
