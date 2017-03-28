from django.core.urlresolvers import reverse
from django.test import override_settings, modify_settings

from tests.test_admin import APIAuthenticatedTestCase


class APIMiddlewareTest(APIAuthenticatedTestCase):
    """
    Test authentication using API key middleware.
    """

    @override_settings(REST_FRAMEWORK={
        'DEFAULT_PERMISSION_CLASSES':
            ('rest_framework.permissions.AllowAny',),
    })
    @modify_settings(MIDDLEWARE={
        'append': 'rest_framework_api_key.middleware.APIKeyMiddleware'
    })
    def test_get_view_authorized(self):
        """
        Test successful authentication.
        """
        response = self.client.get(reverse("test-view"), **self.header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["msg"], "Hello World!")

    @override_settings(REST_FRAMEWORK={
        'DEFAULT_PERMISSION_CLASSES':
            ('rest_framework.permissions.AllowAny',),
    })
    @modify_settings(MIDDLEWARE={
        'append': 'rest_framework_api_key.middleware.APIKeyMiddleware'
    })
    def test_get_view_unauthorized(self):
        """
        Test failed authentication.
        """
        response = self.client.get(reverse("test-view"))

        self.assertEqual(response.status_code, 403)

    @override_settings(REST_FRAMEWORK={
        'DEFAULT_PERMISSION_CLASSES':
            ('rest_framework.permissions.AllowAny',),
    })
    @modify_settings(MIDDLEWARE={
        'append': 'rest_framework_api_key.middleware.APIKeyMiddleware'
    })
    def test_get_view_excluded(self):
        """
        Test not required for paths excluded in settings.
        """
        response = self.client.get(reverse("admin:index"))
        self.assertNotEqual(response.status_code, 403)
