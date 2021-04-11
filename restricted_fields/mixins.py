from collections import OrderedDict

from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject


class RestrictedFieldsSerializerMixin(object):
    """API Serializer mixin

    This provides support for restricting serialized data to only a subset of fields using the
    ``only`` and ``defer`` query parameters.

    :param only: Restricted to only a subset of fields (Include these fields).
    :type only: list
    :param defer: Defer the listed fields (Exclude these fields).
    :type defer: list


    **Example:**

    Serialize only the `id` and `name` fields.

    .. code-block:: console

        GET https://.../api/users/?only=id&only=name

    .. code-block:: console

        {
            "count":1,
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
    """
    RESTRICTED_FIELDS_PARAM = 'only'
    DEFERRED_FIELDS_PARAM = 'defer'

    def to_representation(self, instance):
        """
        Convert Model Object instance -> Dict of primitive datatypes.

        :param instance: The django model instance.
        :type instance: django.db.models.Model
        :return: Dictionary of fields and corresponding value.
        """

        request = self.context['request']
        ret = OrderedDict()
        restricted_fields = request.query_params.getlist(self.RESTRICTED_FIELDS_PARAM)
        deferred_fields = request.query_params.getlist(self.DEFERRED_FIELDS_PARAM)
        fields = self._readable_fields

        if restricted_fields:
            fields = [f for f in fields if f.field_name in restricted_fields]

        if deferred_fields:
            fields = [f for f in fields if f.field_name not in deferred_fields]

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret
