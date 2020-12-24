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
