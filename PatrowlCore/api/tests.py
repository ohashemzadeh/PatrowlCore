from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse


class AddAssetsProductVendorAPITest(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()
        # self.url = '/add-assets-product-vendor-into-monitor-mode'  # API endpoint URL

        self.url = reverse('add-assets-product-vendor-into-monitor-mode')

    def test_valid_post_request(self):
        # Test with valid input data
        data = {
            "asset_name": "Server 1",
            "product_name": "Firewall",
            "vendor_name": "Vendor A"
        }
        response = self.client.post(self.url, data, format='json')

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the response data
        self.assertEqual(response.data['message'], "Asset, product, and vendor added to monitor mode successfully.")
        self.assertEqual(response.data['submitted_data'], data)

    def test_invalid_post_request(self):
        # Test with invalid input data (missing required fields)
        data = {
            "asset_name": "Server 1"
        }
        response = self.client.post(self.url, data, format='json')

        # Assert that the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Assert that the error messages contain the missing fields
        self.assertIn('product_name', response.data)
        self.assertIn('vendor_name', response.data)


class MyAPITestCase(TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)
