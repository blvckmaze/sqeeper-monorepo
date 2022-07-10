from django.db import models
from users.models import User
from . import managers


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    reminder = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True, null=False)
    creation_time = models.TimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(null=False, default=True)

    objects = managers.NoteManager()
