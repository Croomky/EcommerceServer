from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView

from .models import Product,    \
    Category,   \
    FeaturedProduct
from .serializers import ProductDetailsSerializer,  \
    CategoryListSerializer, \
    ProductsByPhraseSerializer, \
    FeaturedProductsSerializer
from .mixins import JsonResponseMixin

class ProductDetails(APIView):
    def get(self, request, id):
        try:
            queryset = Product.objects.get(
                pk=id
            )
            serializer = ProductDetailsSerializer(queryset)
            return JsonResponse(serializer.data)
        except:
            return JsonResponse({
                "error": "No item satisfies given criteria."
            })

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

class FeaturedProducts(
    JsonResponseMixin,
    ListAPIView
):
    queryset = FeaturedProduct.objects.all()
    serializer_class = FeaturedProductsSerializer

    # def get_queryset(self):
    #     for i in self.queryset:
    #         i = i.as_product()

    #     return self.queryset
