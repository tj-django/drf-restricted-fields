from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class TestModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    created_by = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return _(self.name)
