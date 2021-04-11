=====================
drf-restricted-fields
=====================

.. image:: https://img.shields.io/pypi/v/drf_restricted_fields.svg
        :target: https://pypi.python.org/pypi/drf_restricted_fields

.. image:: https://github.com/tj-django/drf-restricted-fields/actions/workflows/test.yml/badge.svg
        :target: https://github.com/tj-django/drf-restricted-fields/actions/workflows/test.yml


.. image:: https://readthedocs.org/projects/drf-restricted-fields/badge/?version=latest
        :target: https://drf-restricted-fields.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/tj-django/drf-restricted-fields/shield.svg
     :target: https://pyup.io/repos/github/tj-django/drf-restricted-fields/
     :alt: Updates


Features
========

Restrict fields returned by DRF serializers using the ``only`` query parameter
------------------------------------------------------------------------------

.. code-block:: console

    GET http://127.0.0.1:8000/api/users/?only=id&only=name


Serialize only the `id` and `name` fields.

.. code-block:: console

    {
        "count": 198,
        "next": "http://127.0.0.1:8000/api/users/?only=id&only=name&page=1",
        "previous": null,
        "results":[
            {
                "id": 1,
                "name": "Test"
            },
            ...
        ],
    }


Defer fields returned by DRF serializers using the ``defer`` query parameter
----------------------------------------------------------------------------

.. code-block:: console

    GET http://127.0.0.1:8000/api/users/?defer=name&defer=age


Serialize only the `id` and `name` fields.

.. code-block:: console

    {
        "count": 198,
        "next": "http://127.0.0.1:8000/api/users/?defer=name&defer=age&page=1",
        "previous": null,
        "results":[
            {
                "id": 1,
            },
            ...
        ],
    }


* Free software: MIT license
* Documentation: https://drf-restricted-fields.readthedocs.io.

