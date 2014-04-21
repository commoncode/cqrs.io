from django.db import models
from django.contrib import admin
from django.core import serializers

import zerorpc
# Create your models here.

# from djangoadmin.settings_cqrs import *
# from mongoengine import *

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    
    
class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        c = zerorpc.Client()
        c.connect("tcp://127.0.0.1:4242")
        product = '{"name":"%s", "description":"%s", "price":"%s"}' % (obj.name, obj.description, obj.price)
        c.hello(product)
        
        obj.save()
