from django.contrib.auth import models as auth_models
from . import models


class UserManager(auth_models.BaseUserManager):
    def create_user(
        self,
        email: str,
        password: str,
        is_staff=False,
        is_superuser=False,
        first_name: str = None,
        last_name: str = None,
    ) -> "models.User":
        assert len(password.strip()) >= 6, "Password is too short"

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        user.save()

        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> "models.User":
        user = self.create_user(
            email,
            password,
            is_staff=True,
            is_superuser=True,
            first_name=first_name,
            last_name=last_name,
        )

        user.save()

        return user
