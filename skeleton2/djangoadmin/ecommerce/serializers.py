from django.contrib.auth.models import User, Group
from rest_framework import serializers

from ecommerce.models import Product, Cart, Oplogqueue

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('name', 'owner')
        

class OplogqueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Oplogqueue
        fields = ('description', 'productname', 'userid')
