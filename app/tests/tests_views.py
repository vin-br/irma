import unittest
import os

from django.conf import settings
from django.test import TestCase
from django.http import HttpRequest
from django.core.files.uploadedfile import SimpleUploadedFile
from app.views import index


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
        self.assertIn(b"uploading your MRI scan", response.content)

    def test_file1_uploaded(self):
        request = HttpRequest()
        request.method = "POST"
        file1 = SimpleUploadedFile("file1.txt", b"ARC Scanner")
        request.FILES = {"file1": file1}
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(os.path.exists(os.path.join(settings.MEDIA_ROOT, "file1.txt")))
        with open(os.path.join(settings.MEDIA_ROOT, "file1.txt"), "rb") as f:
            contents = f.read()
            self.assertEqual(contents, b"ARC Scanner")
        os.unlink(os.path.join(settings.MEDIA_ROOT, "file1.txt"))

    # Not working, to debug in the future
    # def test_no_file1(self):
    #     request = HttpRequest()
    #     request.method = "POST"
    #     request.FILES = {}
    #     response = index(request)
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn("There is no file1 in form!", str(response))


if __name__ == "__main__":
    unittest.main()
