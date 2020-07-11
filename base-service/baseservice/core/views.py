from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.response import Response

from baseservice.core.models import Product, User
from baseservice.core.serializers import ProductSerializer, UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_serializer_context(self):
        return {'user_id': self.request.query_params.get('userId')}

    def list(self, request, *args, **kwargs):
        user_id = self.request.query_params.get('userId')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
            except ObjectDoesNotExist:
                return Response({"error": "User not found"}, status=404)

        return super(ProductViewSet, self).list(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put']
    serializer_class = UserSerializer
    queryset = User.objects.all()
