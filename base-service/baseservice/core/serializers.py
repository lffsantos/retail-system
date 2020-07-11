from rest_framework import serializers

from baseservice.core.client_calculator import get_discount
from baseservice.core.models import User, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)
        self.user_id = self.context["user_id"] or None
        self.conn_failure = False

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        if not self.user_id:
            return data

        if self.conn_failure:
            return data

        try:
            discount = get_discount(instance.id, self.user_id)
            if discount:
                data.update(discount)
        except Exception as e:
            self.conn_failure = True

        return data
