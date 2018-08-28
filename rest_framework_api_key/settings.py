from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'API_KEY_CONFIG', None)

DEFAULTS = {
    'REQUEST_META_KEY': 'HTTP_API_KEY',
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS)
