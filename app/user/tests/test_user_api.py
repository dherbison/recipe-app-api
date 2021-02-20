from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse('user:create')
TOKER_URL = reverse('user:token')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        payload = {
            'email': 'test@appdev.com',
            'password': 'testpass',
            'name': 'Test Name'}
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', response.data)

    def test_user_exists(self):
        payload = {
            'email': 'test@appdev.com',
            'password': 'testpass'}
        create_user(**payload)
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            'email': 'test@appdev.com',
            'password': 'pw', 'name':
                'Test Name'
                   }
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        payload = {'email': 'test@appdev.com', 'password': 'pw'}
        create_user(**payload)
        response = self.client.post(TOKER_URL, payload)

        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_credentials(self):
        create_user(email='test@dan.com', password='testpass')
        payload = {'email': 'test@dan.com', 'password': 'wrong'}
        response = self.client.post(TOKER_URL, payload)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_without_user(self):
        payload = {'email': 'test@dan.com', 'password': 'testpass'}
        response = self.client.post(TOKER_URL, payload)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_fields(self):
        response = self.client.post(TOKER_URL, {
            'email': 'dan',
            'password': ''})
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
