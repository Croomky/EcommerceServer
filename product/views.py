from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import RetrieveAPIView, ListAPIView

from .models import Product, Category
from .serializers import ProductDetailsSerializer, CategoryListSerializer
from .mixins import JsonResponseMixin

class ProductDetails(
    JsonResponseMixin,
    RetrieveAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_url_kwarg = 'id'

class CategoryList(
    JsonResponseMixin,
    ListAPIView
):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return Category.objects.filter(upperCategory=None)