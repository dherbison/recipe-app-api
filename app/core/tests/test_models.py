from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'dan@xxx.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normallized(self):
        email = 'test@DFDSFSFS.COM'
        user = get_user_model().objects.create_user(email, 'tst21132')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """"""
        user = get_user_model().objects.create_superuser(
            'test@long.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
