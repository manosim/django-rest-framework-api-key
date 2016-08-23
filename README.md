# django-rest-framework-api-key [![travis][travis-image]][travis-url] [![codecov][codecov-image]][codecov-url] [![pypi][pypi-image]][pypi-url]
Authenticate Web APIs made with Django REST Framework


### Supports

  - Python (2.7, 3.3, 3.4, 3.5)
  - Django (1.8, 1.9, 1.10)
  - Django Rest Framework (3+)


### Installation

Install using pip:

    pip install drfapikey

Add 'rest_framework_api_key' to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'rest_framework_api_key',
    )

Finally set the django-rest-framework permissions under your django settings:

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework_api_key.permissions.HasAPIAccess',
        )
    }


### Example Request

```python
response = requests.get(
    url="http://uhs-api.ctf.sh:8080/catalogue/categories/",
    headers={
        "Api-Key": "fd8b4a98c8f53035aeab410258430e2d86079c93",
    },
)
```


[travis-image]: https://travis-ci.org/ekonstantinidis/django-rest-framework-api-key.svg?branch=master
[travis-url]: https://travis-ci.org/ekonstantinidis/django-rest-framework-api-key

[codecov-image]: https://codecov.io/github/ekonstantinidis/django-rest-framework-api-key/coverage.svg?branch=master
[codecov-url]:https://codecov.io/github/ekonstantinidis/django-rest-framework-api-key?branch=master

[pypi-image]: https://badge.fury.io/py/drfapikey.svg
[pypi-url]: https://pypi.python.org/pypi/drfapikey/
