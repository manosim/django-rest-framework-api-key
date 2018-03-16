"""
Middleware verifying every request to the server passes the API key validation.
"""
from django.core.exceptions import PermissionDenied

from rest_framework_api_key.helpers import get_key_from_headers
from rest_framework_api_key.models import APIKey


class APIKeyMiddleware(object):
    """
    A custom middleware to provide API key validation for all requests.
    """

    def is_key_valid(self, api_key):
        """
        A wrapper function around api key validation, to make the
        process more generic and easier to mock.

        :param api_key: The api key value from the request.
        :type api_key: str
        :return: Whether the key has been registered.
        :rtype: bool
        """
        return APIKey.is_valid(api_key)

    def process_request(self, request):
        """
        Middleware processing method, API key validation happens here.

        :param request: The HTTP request.
        :type request: :class:`django.http.HttpRequest`
        :returns: The HTTP response.
        :rtype: :class:`django.http.HttpResponse`
        """
        api_key = get_key_from_headers(request)
        api_key_object = APIKey.objects.filter(key=api_key).first()
        if not self.is_key_valid(api_key):
            raise PermissionDenied('API key missing or invalid.')

        request.api_key = api_key_object
