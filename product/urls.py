from django.contrib import admin
from django.urls import path, include

from .views import ProductDetails,  \
    CategoryList,   \
    ProductsByPhrase,   \
    FeaturedProducts,   \
    ProductByCategory

urlpatterns = [
    path('details/<int:id>', ProductDetails.as_view()),
    path('categoryList', CategoryList.as_view()),
    path('search', ProductsByPhrase.as_view()),
    path('featuredProductList', FeaturedProducts.as_view()),
    path('byCategory/<int:category_id>', ProductByCategory.as_view())
]
