import copy
from unittest import mock

from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json

from baseservice.core.models import Product, User

PRODUCTS = [{
    "id": 1,
    "title": "Produto 1",
    "description": "produto 1",
    "price": "100.00",
    "base_discount_percent": 0.1
}, {
    "id": 2,
    "title": "Produto 2",
    "description": " produto 2",
    "price": "30.00",
    "base_discount_percent": 5.0
}, {
    "id": 3,
    "title": "Produto 3",
    "description": "produto 3",
    "price": "90.00",
    "base_discount_percent": 15.0
}, {
    "id": 4,
    "title": "Produto 4",
    "description": "produto 4",
    "price": "150.00",
    "base_discount_percent": 10.0
}]

USERS = [{
    "id": 1,
    "first_name": "Lucas",
    "last_name": "Farias",
    "birthdate": "1987-03-23"
}, {
    "id": 2,
    "first_name": "Jose",
    "last_name": "Alves",
    "birthdate": "2000-01-20"
},{
    "id": 3,
    "first_name": "Maria",
    "last_name": "Clara",
    "birthdate": "1990-11-11"
}]


class TestProductView(APITestCase):

    def setUp(self):
        self.quantity = 4
        self.products = copy.deepcopy(PRODUCTS)
        for product in PRODUCTS:
            Product.objects.create(**product)
        for user in USERS:
            User.objects.create(**user)

    @parameterized.expand([(1, ), (2, ), (None, )])
    @mock.patch('baseservice.core.client_calculator.get_discount',
                mock.MagicMock(return_value={"total_discount": 5.1, "final_price": 94.9}))
    def test_product_list(self, user_id):
        filter_user = ''
        if user_id:
            filter_user = f"?userId={user_id}"

        url = '/products/'+filter_user
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(PRODUCTS))

        # When don't have user_id don't show total_discount and final price
        if not user_id:
            for index, product in enumerate(PRODUCTS):
                self.assertEqual(json.dumps(response.data[index]), json.dumps(product))
        else:
            for p in self.products:
                p['total_discount'] = 5.1
                p['final_price'] = 94.9

            for index, product in enumerate(self.products):
                self.assertEqual(json.dumps(response.data[index]), json.dumps(product))
