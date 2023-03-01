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

    def _if_skip_api_key_check(self, request):
        if request.method == 'OPTIONS' or request.path.find('/api/') < 0 or request.path == '/redemptions/api/mobile_topup_callback/':
            return True

        u_agent = request.META.get('HTTP_USER_AGENT', "")
        if "Darwin" in u_agent or u_agent.startswith("Mozilla") or u_agent.startswith("Opera") or u_agent.startswith("Slackbot"):
            return True

        if u_agent.startswith("ELB-HealthChecker"):
            return True

        if "skor/" in u_agent.lower() and "tts app" not in u_agent.lower() and "move" not in u_agent.lower() and "myaia" not in u_agent.lower():
            return True

        return False

    def process_request(self, request):
        """
        Middleware processing method, API key validation happens here.

        :param request: The HTTP request.
        :type request: :class:`django.http.HttpRequest`
        :returns: The HTTP response.
        :rtype: :class:`django.http.HttpResponse`
        """

        if self._if_skip_api_key_check(request):
            # for backward compatible, we don't check api_key for skor apps, but when they send in one, we find it
            api_key = get_key_from_headers(request)
            if api_key:
                api_key_object = APIKey.objects.filter(key=api_key).first()
                request.api_key = api_key_object
            else:
                request.api_key = None
        else:
            api_key = get_key_from_headers(request)
            api_key_object = APIKey.objects.filter(key=api_key).first()
            if not api_key_object or not api_key_object.is_valid(request.path):
                raise PermissionDenied('API key missing or invalid.')

            request.api_key = api_key_object
