from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse


class AddAssetsProductVendorAPITest(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()

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


class SwaggerTests(TestCase):

    def test_swagger_ui(self):
        # Test that the Swagger UI loads correctly
        url = reverse('swagger-ui')  # URL name for the Swagger UI
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_redoc_ui(self):
        # Test that the Redoc UI loads correctly
        url = reverse('redoc')  # URL name for the Redoc UI
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_openapi_schema(self):
        # Test that the OpenAPI schema generates correctly
        url = reverse('schema')  # URL name for the OpenAPI schema
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
