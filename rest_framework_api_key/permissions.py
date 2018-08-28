from rest_framework import permissions
from rest_framework_api_key.models import APIKey
from .settings import api_settings


class HasAPIAccess(permissions.BasePermission):
    message = 'Invalid or missing API Key.'

    def has_permission(self, request, view):
        api_key = request.META.get(api_settings.REQUEST_META_KEY, '')
        return APIKey.objects.filter(key=api_key).exists()
