"""
Middleware verifying every request to the server passes the API key validation.
"""
from django.conf import settings
from django.core.exceptions import PermissionDenied

from rest_framework_api_key.helpers import get_key_from_headers
from rest_framework_api_key.models import APIKey


# Loaded dynamically to handle cases where the settings variable is not defined.
excluded_prefixes = getattr(settings, 'API_KEY_MIDDLEWARE_EXCLUDED_URL_PREFIXES', ())


class APIKeyMiddleware(object):
    """
    A custom middleware to provide API key validation for all requests.
    """

    def __init__(self, get_response):
        """
        The middleware initialization method.

        :param get_response: The response rendering view.
        :type get_response: function
        """
        self.get_response = get_response

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

    def __call__(self, request):
        """
        Middleware processing method, API key validation happens here.

        :param request: The HTTP request.
        :type request: :class:`django.http.HttpRequest`
        :returns: The HTTP response.
        :rtype: :class:`django.http.HttpResponse`
        """
        response = self.get_response(request)

        if request.path.startswith(excluded_prefixes):
            return response

        api_key = get_key_from_headers(request)
        if not self.is_key_valid(api_key):
            raise PermissionDenied('API key missing or invalid.')

        return response
