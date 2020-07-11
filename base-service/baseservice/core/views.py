from rest_framework import viewsets

from baseservice.core.models import Product, User
from baseservice.core.serializers import ProductSerializer, UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = UserSerializer
    queryset = User.objects.all()
