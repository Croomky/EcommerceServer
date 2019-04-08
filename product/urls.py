from django.contrib import admin
from django.urls import path, include

from .views import ProductDetails

urlpatterns = [
    path('details/<int:id>', ProductDetails.as_view())
]
