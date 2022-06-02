from http import HTTPStatus

from django.test import TestCase, Client


class APITests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_category_url(self):
        response = self.guest_client.get('/api/v1/categories/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_genre_url(self):
        response = self.guest_client.get('/api/v1/genres/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_title_url(self):
        response = self.guest_client.get('/api/v1/titles/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertNotEqual(response.status_code, HTTPStatus.NOT_FOUND)
