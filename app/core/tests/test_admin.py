from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='amdin@dan.com',
            password='pawsre24343'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='tset@fasfdsf.com',
                                                         password='sfafsd2323',
                                                         name='test user full name')

    def test_users_listed(self):
        """ reverse creates URLs """
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        # /admin/core/user/<user id>
        url = reverse('admin:core_user_change',args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        url = reverse('admin:core_user_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
