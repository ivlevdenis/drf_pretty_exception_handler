Django Rest Framework pretty exception handler
==============================================


![https://pypi.python.org/pypi/drf_pretty_exception_handler](https://img.shields.io/pypi/v/drf_pretty_exception_handler.svg) ![https://travis-ci.com/ivlevdenis/drf_pretty_exception_handler](https://img.shields.io/travis/ivlevdenis/drf_pretty_exception_handler.svg) ![https://drf-pretty-exception-handler.readthedocs.io/en/latest/?badge=latest](https://readthedocs.org/projects/drf-pretty-exception-handler/badge/?version=latest) ![https://pyup.io/repos/github/ivlevdenis/drf_pretty_exception_handler/](https://pyup.io/repos/github/ivlevdenis/drf_pretty_exception_handler/shield.svg)

Django Rest Framework pretty exception handler


* Free software: MIT license


Features
--------

Default Django Rest Framework exception handler return errors in different formats.

**Examples**:
Response on `raise exceptions.APIException`.
```json
{
  "detail": "A server error occurred."
}
```
Response on `raise exceptions.ValidationError`.
```json
[
  "Invalid input."
]
```
Response on `raise exceptions.ValidationError` if error in field serializator.
```json
{
  "email": [
    "This field is required."
  ]
}
```
Response on `raise exceptions.ValidationError` in serializator `.validate()` .
```json
{
  "non_field_errors": [
    "Passwords does not match"
  ]
}
```


This greatly complicates error handling in the frontend. This package provide own format of errors.

```json
{
  "status_code": 500,
  "errors": {
    "non_field_errors": [
      "A server error occurred."
    ]
  }
}
```

```json
{
  "status_code": 400,
  "errors": {
    "non_field_errors": [
      "Invalid input."
    ]
  }
}
```
```json
{
  "status_code": 400,
  "errors": {
    "email": [
      "This field is required."
    ]
  }
}
```
```json
{
  "status_code": 400,
  "errors": {
    "non_field_errors": [
      "Passwords does not match"
    ]
  }
}
```

And this package handle default Python exceptions.
```python
l = [1, 2, 3, 4]
l[10]
```

```json
{
  "status_code": 500,
  "errors": {
    "non_field_errors": [
      "IndexError: list index out of range"
    ]
  }
}
```
<!-- * TODO -->

Credits
-------

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
