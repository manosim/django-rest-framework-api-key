from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.helpers import generate_key


class LoggedInAdminTestCase(TestCase):

    USERNAME = "martymcfly"
    EMAIL = "marty@mcfly.com"
    PASSWORD = "password"

    def setUp(self):
        super(LoggedInAdminTestCase, self).setUp()

        self.user = User.objects.create_superuser(self.USERNAME, self.EMAIL, self.PASSWORD)
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.user.is_superuser)
        self.client.login(username=self.USERNAME, password=self.PASSWORD)


class APIAuthenticatedTestCase(TestCase):

    APP_NAME = 'Project Tests'

    def setUp(self):
        self.app_key = APIKey.objects.create(name=self.APP_NAME, key=generate_key())
        self.header = {'HTTP_API_KEY': self.app_key.key}


class AdminTestCase(LoggedInAdminTestCase, APIAuthenticatedTestCase):
    def setUp(self):
        super(AdminTestCase, self).setUp()
        self.add_app_url = reverse('admin:rest_framework_api_key_apikey_add')

    def test_admin_create_app_access(self):
        response = self.client.get(self.add_app_url)
        self.assertEqual(response.status_code, 200)

    def test_admin_create_app(self):
        self.assertEqual(APIKey.objects.all().count(), 1)

        response = self.client.post(self.add_app_url, data={"name": "Hello"}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please note it since you will not be able to see it again.")
        self.assertContains(response, "was added successfully.")

        self.assertEqual(APIKey.objects.all().count(), 2)

    def test_admin_change_app(self):
        self.change_app_url = reverse('admin:rest_framework_api_key_apikey_change', args=(self.app_key.id,))

        response = self.client.get(self.change_app_url,)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hidden")
