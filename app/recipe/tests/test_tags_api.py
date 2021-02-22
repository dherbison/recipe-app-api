from core.models import Tag
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from recipe.serializers import TagSerializer
from rest_framework import status
from rest_framework.test import APIClient

TAGS_URL = reverse('recipe:tag-list')


class PublicTagsApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@user.com',
            'password123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Dessert')

        res = self.client.get(TAGS_URL)

        # '-' for reverse order
        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        user2 = get_user_model().objects.create_user(
            'other@user.com',
            'password123'
        )
        Tag.objects.create(user=user2, name='Fruity')
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Dessert')

        res = self.client.get(TAGS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data[0]['name'], tag.name)