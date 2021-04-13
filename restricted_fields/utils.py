import typing

from django.http import QueryDict


def get_fields(query_params, key):
    # type: (QueryDict, str) -> typing.Set[str]
    """
    Return a flat list of fields the request

    :param query_params: The request MultiDict instance.
    :type query_params: `django.http.QueryDict`
    :param key: The key to be accessed from the request.
    :type key: str
    :return: Flat list of all fields
    :rtype: set
    """
    values = set()
    last_value = query_params.get(key)
    all_values = query_params.getlist(key)

    if "," in last_value:
        values |= last_value.split(",")
    else:
        values.add(last_value)

    for value in all_values:
        if "," in value:
            values |= value.split(",")
        else:
            values.add(value)

    return values
