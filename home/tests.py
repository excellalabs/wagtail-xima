__author__ = 'Nick'
from django.test import TestCase
from django.test.client import Client

class SimpleTest(TestCase):
    def test_basic_addition(self):
        
        self.assertEqual(1 + 1, 2)
