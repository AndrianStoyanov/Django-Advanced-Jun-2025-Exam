from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.managers import AppUserManager

# Create your models here.


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        unique=True,
    )

    username = models.CharField(
        max_length=150,
        verbose_name='Username',
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )

    objects = AppUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE, primary_key=True, related_name='profile',
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
    position = models.CharField(max_length=100, blank=True, null=True)
    company_job = models.CharField(max_length=70, blank=True, null=True)

    @property
    def profiles_name(self):
        return f"{self.first_name or ''}  {self.last_name or ''}"