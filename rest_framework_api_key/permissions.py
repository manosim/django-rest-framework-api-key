from rest_framework import permissions
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.helpers import get_key_from_headers


class HasAPIAccess(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        api_key = get_key_from_headers(request)
        return APIKey.is_valid(api_key)
