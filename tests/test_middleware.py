from django.test import override_settings, modify_settings

from django.core.urlresolvers import reverse
from tests.test_admin import APIAuthenticatedTestCase


class APIMiddlewareTest(APIAuthenticatedTestCase):

    @override_settings(REST_FRAMEWORK={
        'DEFAULT_PERMISSION_CLASSES':
            ('rest_framework.permissions.AllowAny',),
    })
    @modify_settings(MIDDLEWARE_CLASSES={
        'prepend': 'rest_framework_api_key.middleware.APIKeyMiddleware'
    })
    def test_get_view_authorized(self):
        response = self.client.get(reverse("test-view"), **self.header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["msg"], "Hello World!")

    @override_settings(REST_FRAMEWORK={
        'DEFAULT_PERMISSION_CLASSES':
            ('rest_framework.permissions.AllowAny',),
    })
    @modify_settings(MIDDLEWARE_CLASSES={
        'prepend': 'rest_framework_api_key.middleware.APIKeyMiddleware'
    })
    def test_get_view_unauthorized(self):
        response = self.client.get(reverse("test-view"))

        self.assertEqual(response.status_code, 403)
