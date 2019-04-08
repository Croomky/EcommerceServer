from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import RetrieveAPIView

from .models import Product
from .serializers import ProductDetailsSerializer
from .mixins import JsonResponseMixin

class ProductDetails(
    JsonResponseMixin,
    RetrieveAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_url_kwarg = 'id'
