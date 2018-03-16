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
        if not api_key_object or not api_key_object.is_valid(request.path):
            raise PermissionDenied('API key missing or invalid.')

        request.api_key = api_key_object
