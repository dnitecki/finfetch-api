import dataclasses
from . import models
import datetime
import jwt
from django.conf import settings
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models import User



@dataclasses.dataclass
class UserDataClass:
    email: str
    password :str = None
    id: int = None
    created: str = None


    @classmethod
    def from_instance(cls, user: "User") -> "UserDataClass":
        return cls(
            email=user.email,
            id=user.id,
            created = user.created

        )

def create_user(user: "UserDataClass") -> "UserDataClass":
    instance = models.User(
        email = user.email,
    )
    if user.password is not None:
        instance.set_password(user.password)

    instance.save()

    return UserDataClass.from_instance(instance)

def user_email_selector(email: str) -> "User":
    user = models.User.objects.filter(email=email).first()

    return user

def create_token(user_id: int) -> str:
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow()
    )
    token = jwt.encode(payload, settings.JWT_SECRET, algorith="HS256")

    return token