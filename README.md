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
    url="http://0.0.0.0:8000/api/login",
    headers={
        "Api-Key": "fd8b4a98c8f53035aeab410258430e2d86079c93",
    },
)
```


### Tests
    
    pyvenv env
    source env/bin/activate
    pip install -r requirements/requirements-testing.txt
    python runtests.py


### Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
6. Make sure tests are passing


[travis-image]: https://travis-ci.org/ekonstantinidis/django-rest-framework-api-key.svg?branch=master
[travis-url]: https://travis-ci.org/ekonstantinidis/django-rest-framework-api-key

[codecov-image]: https://codecov.io/github/ekonstantinidis/django-rest-framework-api-key/coverage.svg?branch=master
[codecov-url]:https://codecov.io/github/ekonstantinidis/django-rest-framework-api-key?branch=master

[pypi-image]: https://badge.fury.io/py/drfapikey.svg
[pypi-url]: https://pypi.python.org/pypi/drfapikey/
