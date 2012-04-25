from django.db import models
from sentry.models import Group
from django.contrib.auth.models import User


class Notation(models.Model):
    group = models.OneToOneField(Group, primary_key=True,
        related_name='notation')

    note = models.TextField(default='')
    modified_when = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, blank=True, null=True,
        on_delete=models.SET_NULL)
