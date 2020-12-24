from django.test import TestCase, Client
from django.urls import reverse


class TestLengthConversion(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('length:convert')

    def test_centimetre_to_metre_conversion(self):

        data = {
            "input_unit": "centimetre",
            "output_unit": "metre",
            "input_value": round(8096.894, 3),
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, 80.969)

    def test_metre_to_centimetre_conversion(self):

        data = {
            "input_unit": "metre",
            "output_unit": "centimetre",
            "input_value": 80.969,
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, 8096.9)

    def test_centimetre_to_mile_conversion(self):
        data = {
            "input_unit": "centimetre",
            "output_unit": "mile",
            "input_value": round(985805791.3527409, 3),
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, 6125.511)

    def test_mile_to_centimetre_conversion(self):
        data = {
            "input_unit": "mile",
            "output_unit": "centimetre",
            "input_value":  6125.511,
        }

        response = self.client.get(self.url, data)

        self.assertContains(response, round(985802987.274, 3))
