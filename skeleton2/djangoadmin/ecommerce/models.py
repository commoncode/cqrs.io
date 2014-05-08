from django.db import models
from django.contrib import admin
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver

import zerorpc
# Create your models here.

# from djangoadmin.settings_cqrs import *
# from mongoengine import *

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    
class Cart(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    
    
class Oplogqueue(models.Model):
    description = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)



class OplogqueueAdmin(admin.ModelAdmin):
    list_display = ('description', 'productname', 'status', 'userid')
    
class CartAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

    
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'description', 'price')
    
    '''
    def save_model(self, request, obj, form, change):
        c = zerorpc.Client()
        c.connect("tcp://127.0.0.1:4242")
        product = '{"name":"%s", "description":"%s", "price":"%s"}' % (obj.name, obj.description, obj.price)
        c.hello(product)
        
        obj.save()
        
    '''
        
        
@receiver(post_save, sender=Product)
def send_product_to_zerorpc(sender, instance, **kwargs):
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")
    product = '{"name":"%s", "description":"%s", "price":"%s"}' % (instance.name, instance.description, instance.price)
    c.save_product(product)

    
@receiver(post_save, sender=Cart)
def send_cart_product_to_zerorpc(sender, instance, **kwargs):
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4243")
    cart = '{"name": "%s", "owner": "%s"}' % (instance.name, instance.owner)
    c.save_product_to_cart(cart)
    


