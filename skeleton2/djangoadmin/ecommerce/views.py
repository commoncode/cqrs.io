from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ecommerce.serializers import UserSerializer, GroupSerializer, ProductSerializer

from ecommerce.models import Product

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
