=====================
drf-restricted-fields
=====================


.. image:: https://img.shields.io/pypi/v/drf_restricted_fields.svg
        :target: https://pypi.python.org/pypi/drf_restricted_fields

.. image:: https://img.shields.io/travis/tj-django/drf_restricted_fields.svg
        :target: https://travis-ci.com/tj-django/drf_restricted_fields

.. image:: https://readthedocs.org/projects/drf-restricted-fields/badge/?version=latest
        :target: https://drf-restricted-fields.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/tj-django/drf_restricted_fields/shield.svg
     :target: https://pyup.io/repos/github/tj-django/drf_restricted_fields/
     :alt: Updates



Restrict fields returned by DRF serializers

.. code-block:: sh

    GET http://127.0.0.1:8000/api/users/?only=id&only=name


Serialize only the `id` and `name` fields.

.. code-block:: json

    {
        "count":198,
        "next": "http://127.0.0.1:8000/api/users/?only=id&only=name&page=1",
        "previous":null,
        "results":[
            {
                "id":1,
                "name": "Test"
            },
            ...
        ],
    }


* Free software: MIT license
* Documentation: https://drf-restricted-fields.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
