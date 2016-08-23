from django.test import TestCase
from rest_framework_api_key.models import APIKey


class ModelTestCase(TestCase):

    def setUp(self):
        super(ModelTestCase, self).setUp()

    def test_admin_create_object(self):
        self.assertEqual(APIKey.objects.all().count(), 0)
        APIKey.objects.create(name="Hello World", key="helloworld")
        self.assertEqual(APIKey.objects.all().count(), 1)
