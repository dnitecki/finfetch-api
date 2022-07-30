from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone

class UserManager(auth_models.BaseUserManager):
    def create_user(self, email: str, password: str = None, is_staff=False, is_superuser=False) -> "User":
        if not email:
            raise ValueError("User must have an email")
        
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
        
    def create_superuser(self, email: str, password: str) -> "User":
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        user.save()

        return user

class User(auth_models.AbstractUser):
    email = models.EmailField( verbose_name="Email", max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    created = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []



