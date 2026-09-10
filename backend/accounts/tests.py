from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class AuthenticationAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

    def test_login(self):
        response = self.client.post(
            '/api/auth/login/',
            {
                'username': 'testuser',
                'password': 'testpass123'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_invalid_login(self):
        response = self.client.post(
            '/api/auth/login/',
            {
                'username': 'testuser',
                'password': 'wrongpassword'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_me_without_authentication(self):
        response = self.client.get('/api/auth/me/')

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )