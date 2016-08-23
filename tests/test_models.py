from django.test import TestCase
from rest_framework_api_key.models import APIKey


class APIKeyAdminTestCase(TestCase):

    def setUp(self):
        super(APIKeyAdminTestCase, self).setUp()

    def test_admin_create_object(self):
        self.assertEqual(APIKey.objects.all().count(), 0)
        APIKey.objects.create(name="Hello World", key="helloworld")
        self.assertEqual(APIKey.objects.all().count(), 1)
