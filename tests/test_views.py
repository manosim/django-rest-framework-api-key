from django.core.urlresolvers import reverse
from tests.test_admin import APIAuthenticatedTestCase


class APICategoriesEndpoint(APIAuthenticatedTestCase):

    def test_get_view_authorized(self):

        response = self.client.get(reverse("test-view"), **self.header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["msg"], "Hello World!")

    def test_get_view_unauthorized(self):

        response = self.client.get(reverse("test-view"))

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data["detail"], "Authentication credentials were not provided.")
