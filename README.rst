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

.. image:: https://img.shields.io/lgtm/alerts/g/tj-django/drf-restricted-fields.svg?logo=lgtm&logoWidth=18
     :target: https://lgtm.com/projects/g/tj-django/drf-restricted-fields/alerts/
     :alt: Total alerts

.. image:: https://img.shields.io/lgtm/grade/python/g/tj-django/drf-restricted-fields.svg?logo=lgtm&logoWidth=18
     :target: https://lgtm.com/projects/g/tj-django/drf-restricted-fields/context:python
     :alt: Language grade: Python


Installation
============

.. code-block:: console

    pip install drf-restricted-fields


Usage
=====

``serializer.py``

.. code-block:: python
    
    from rest_framework import serializers
    from restricted_fields import RestrictedFieldsSerializerMixin
    
    User = get_user_model()
    
    
    class UserSerializer(RestrictedFieldsSerializerMixin, serializers.ModelSerializer)
        
        class Meta:
            model = User
            fields = (
                'id',
                'name',
                'email',
                'is_staff',
            )
            
``api/views.py`` 

.. code-block:: python

    from rest_framework import viewsets
    
    from my_app.api.serializer import UserSerializer
    
    User = get_user_model()

    
    class UserViewSet(viewsets.ReadOnlyModelViewSet):
        """
        API endpoint to retrieve all users
        """
        queryset = User.objects.all()
        serializer_class = UserSerializer


Features
========

Restrict fields returned by DRF serializers using the ``only`` query parameter
------------------------------------------------------------------------------

.. code-block:: console

    GET http://127.0.0.1:8000/api/users/?only=id&only=name


Serialize only the ``id`` and ``name`` fields.

.. code-block:: console

    {
        "count": 198,
        "next": "http://127.0.0.1:8000/api/users/?only=id&only=name&page=2",
        "previous": null,
        "results":[
            {
                "id": 1,
                "name": "Test user"
            },
            ...
        ],
    }


Defer fields returned by DRF serializers using the ``defer`` query parameter
----------------------------------------------------------------------------

.. code-block:: console

    GET http://127.0.0.1:8000/api/users/?defer=name&defer=is_staff


Serialize all except the ``name`` and ``is_staff`` fields.

.. code-block:: console

    {
        "count": 198,
        "next": "http://127.0.0.1:8000/api/users/?defer=name&defer=age&page=2",
        "previous": null,
        "results":[
            {
                "id": 1,
                "email": "test@test.com"
            },
            ...
        ],
    }


* Free software: MIT license
* Documentation: https://drf-restricted-fields.readthedocs.io.
