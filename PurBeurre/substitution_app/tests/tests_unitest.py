import json
import requests
import unittest

from django.test import TestCase
from django.http import Http404
from ..callapi import Callapi


class Callapipourvoir(unittest.TestCase):
    def test_1_request_the_openfoodfact_api_response_url(self):
        self.query = "pytest"
        apicall = Callapi()
        response = apicall.request_the_openfoodfact_api(self.query)
        self.assertIsInstance(response, dict)
        
    def test_2_request_the_openfoodfact_api_response(self):
        self.query = 'nutella'
        apicall = Callapi()
        assert 'products' in apicall.request_the_openfoodfact_api(self.query)
        assert 'product_name_fr' in apicall.request_the_openfoodfact_api(self.query)['products'][0]
        assert 'image_small_url' in apicall.request_the_openfoodfact_api(self.query)['products'][0]
        assert 'code' in apicall.request_the_openfoodfact_api(self.query)['products'][0]
        assert 'categories_hierarchy' in apicall.request_the_openfoodfact_api(self.query)['products'][0]
        assert 'nutrition_grade_fr' in apicall.request_the_openfoodfact_api(self.query)['products'][0]

    def test_3_clean_the_openfoodfact_api_request(self):
        apicall = Callapi()
        self.query = 'nutella'
        self.response = apicall.request_the_openfoodfact_api(self.query)
        self.clean_response = {
            'product_name': 'Nutella', 'code': '3017620429484', 'nutrition_grade_fr': 'e', 'categories_hierarchy': 
                ['fr:pates-a-tartiner'], 
                'categories': 'Produits à tartiner, Petit-déjeuners, Produits à tartiner sucrés, Pâtes à tartiner, Pâtes à tartiner aux noisettes, Pâtes à tartiner au chocolat, Pâtes à tartiner aux noisettes et au cacao', 
                'image_small_url': 'https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.200.jpg'
                }
        assert apicall.clean_the_openfoodfact_api_request(self.response)[0] == self.clean_response

    def test_4_barcode_request_the_openfoodfact_api(self):
        apicall = Callapi()
        self.barcode = '3017620429484'
        assert 'product' in apicall.barcode_request_the_openfoodfact_api(self.barcode)
        assert 'product_name_fr' in apicall.barcode_request_the_openfoodfact_api(self.barcode)['product']
        assert 'image_small_url' in apicall.barcode_request_the_openfoodfact_api(self.barcode)['product']
        assert 'code' in apicall.barcode_request_the_openfoodfact_api(self.barcode)['product']
        assert 'categories_hierarchy' in apicall.barcode_request_the_openfoodfact_api(self.barcode)['product']
        assert 'nutrition_grade_fr' in apicall.barcode_request_the_openfoodfact_api(self.barcode)['product']

    def test_5_barcode_clean_the_oppenfoodfact_api_request(self):
        apicall = Callapi()
        self.barcode = '3017620429484'
        self.response = apicall.barcode_request_the_openfoodfact_api(self.barcode)
        self.clean_response = {
            'product_name_fr': 'Nutella', 'code': '3017620429484', 'nutrition_grade_fr': 'e', 'categories_hierarchy': 
            ['fr:pates-a-tartiner'], 
            'categories': 'Produits à tartiner, Petit-déjeuners, Produits à tartiner sucrés, Pâtes à tartiner, Pâtes à tartiner aux noisettes, Pâtes à tartiner au chocolat, Pâtes à tartiner aux noisettes et au cacao', 
            'image_small_url': 'https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.200.jpg'
            }
        assert apicall.barcode_clean_the_oppenfoodfact_api_request(self.response) == self.clean_response

    def test_6_request_for_substitution_products_in_openfoodfact_api(self):
        apicall = Callapi()
        self.barcode = '3017620429484'
        self.apiQuery = apicall.barcode_request_the_openfoodfact_api(self.barcode)
        self.apiQuery = apicall.barcode_clean_the_oppenfoodfact_api_request(self.apiQuery)
        assert 'products' in apicall.request_for_substitution_products_in_openfoodfact_api(self.apiQuery)

