from datetime import datetime, timedelta
from dataclasses import dataclass
from django.conf import settings
from .models import User
import jwt


@dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    password: str
    id: int = None

    @classmethod
    def from_instance(cls, user: "User") -> "UserData":
        return cls(
            id=user.id,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
        )


def create_user(user: "UserData") -> UserData:
    instance = User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    if user.password:
        instance.set_password(user.password)

    instance.save()

    return UserData.from_instance(instance)


def user_email_selector(email: str) -> "User":
    return User.objects.filter(email=email).first()


def user_create_token(uid: int) -> str:
    current_time = datetime.utcnow()

    payload = dict(
        id=uid,
        exp=current_time + timedelta(hours=24),
        iat=current_time,
    )

    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
