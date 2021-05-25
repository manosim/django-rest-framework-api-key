from django.test import override_settings, modify_settings

from django.core.urlresolvers import reverse
from tests.test_admin import APIAuthenticatedTestCase


@override_settings(REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':
        ('rest_framework.permissions.AllowAny',),
})
@modify_settings(MIDDLEWARE_CLASSES={
    'prepend': 'rest_framework_api_key.middleware.APIKeyMiddleware'
})
class APIMiddlewareTest(APIAuthenticatedTestCase):

    def test_get_view_authorized(self):
        response = self.client.get(reverse("test-view"), **self.header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["msg"], "Hello World!")

    def test_get_view_unauthorized(self):
        response = self.client.get(reverse("test-view"))
        self.assertEqual(response.status_code, 403)
        self.assertContains(response, 'Authentication credentials were not provided', status_code=403)

    def test_get_api_view_authorized(self):
        response = self.client.get(reverse("test-api-view"), **self.header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["msg"], "Hello API!")

    def test_get_api_view_rejected(self):
        response = self.client.get(reverse("test-api-view"))

        self.assertEqual(response.status_code, 403)
        self.assertContains(response, '403 Forbidden', status_code=403)

    def test_get_api_view_unauthorized_with_special_user_agents(self):
        for agent in [
            'ELB-HealthChecker/2.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X Safari/537.36',
            'Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18',
            'Skor/6 iOS | iPhone11,2 | 13.1.2 | 1.0.35',
            'CerraPoint/150 CFNetwork/1107.1 Darwin/19.0.0',
        ]:

            response = self.client.get(reverse("test-api-view"), **{'HTTP_USER_AGENT': agent})

            self.assertEqual(response.status_code, 403)
            self.assertContains(response, 'Authentication credentials were not provided', status_code=403)

    def test_tts_app_rejected_without_api_key(self):
        response = self.client.get(reverse("test-api-view"), **{'HTTP_USER_AGENT': 'Skor/2 tts app'})

        self.assertEqual(response.status_code, 403)
        self.assertContains(response, '403 Forbidden', status_code=403)

    def test_move_app_rejected_without_api_key(self):
        response = self.client.get(reverse("test-api-view"), **{'HTTP_USER_AGENT': 'Skor/9 Move Backend'})

        self.assertEqual(response.status_code, 403)
        self.assertContains(response, '403 Forbidden', status_code=403)
