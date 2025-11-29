import unittest
from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get("https://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 200)

    def test_wrong_index_404_response(self):
        """Wrong index returns 404 properly"""
        response = self.client.get("http://127.0.0.1:8000/home")
        self.assertEqual(response.status_code, 404)

    def test_wrong_route_404_response(self):
        """Wrong address returns 404 properly"""
        response = self.client.get("http://127.0.0.1:8000/arc")
        self.assertEqual(response.status_code, 404)

    def test_index_page_for_title(self):
        """The index page loads properly and has the title 'ARC'"""
        response = self.client.get("https://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ARC", response.content)

    def test_index_page_for_content(self):
        """The index page loads properly and has the content regarding the upload"""
        response = self.client.get("https://127.0.0.1:8000/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Select your image", response.content)


if __name__ == "__main__":
    unittest.main()
