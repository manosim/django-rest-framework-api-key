import binascii
import os


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


def get_key_from_headers(request):
    return request.META.get('HTTP_API_KEY', '')
