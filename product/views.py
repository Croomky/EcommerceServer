from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from rest_framework.generics import RetrieveAPIView, ListAPIView

from .models import Product, Category
from .serializers import ProductDetailsSerializer,  \
    CategoryListSerializer, \
    ProductsByPhraseSerializer
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

class ProductsByPhrase(
    JsonResponseMixin,
    ListAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductsByPhraseSerializer

    def get_queryset(self):
        phrase = self.request.query_params.get('q')
        criterion_name = Q(name__contains=phrase)
        criterion_desc = Q(description__contains=phrase)
        criterion_body = Q(body__contains=phrase)
        return Product.objects.filter(
            criterion_name
            or criterion_desc
            or criterion_body
        )