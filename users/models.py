from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from post.validators import validate_password, validate_email_domain, validate_age


class CustomUserManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError("The Login field must be set")
        email = extra_fields.get('email')
        if email:
            validate_email_domain(email)
        user = self.model(login=login, **extra_fields)
        if password:
            validate_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(login, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=255, unique=True, default='temporary_login')
    phone_number = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True, validators=[validate_age])
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True, validators=[validate_email_domain], null=True, blank=True)
    password = models.CharField(max_length=128, validators=[validate_password])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login
