from django.contrib.auth import models as auth_models
from django.db import models
from . import managers


class User(auth_models.AbstractUser):
    user_permissions, groups, username = None, None, None

    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, max_length=255)

    objects = managers.UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password", "first_name", "last_name"]
