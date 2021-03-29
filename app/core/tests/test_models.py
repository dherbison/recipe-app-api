from core import models
from django.contrib.auth import get_user_model
from django.test import TestCase


def sample_user(email='test@dherbison.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


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

    def test_create_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        # this set() fx is the __str__ function in the
        # Tag.__str__ method in the models.py file.
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushroom sauce',
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(recipe), recipe.title)
