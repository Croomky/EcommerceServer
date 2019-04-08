from os import path 
from django.db import models
from django.contrib import admin
from ecommerceserver.settings import STATIC_ROOT

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    upperCategory = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)# short description of a product
    thumbnail = models.ImageField(upload_to='thumbnails')
    price = models.FloatField()
    availableAmt = models.FloatField()
    body = models.TextField(max_length=5000)# actual text appearing on a product detail site
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_thumbnail_name(self):
        return self.thumbnail.name.split('/')[-1]

class Image(models.Model):
    img = models.ImageField()
    description = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.__str__() + ' img'

class FeaturedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

admin.site.register(Product)
