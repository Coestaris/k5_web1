import uuid

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class URL(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.CharField(max_length=2048)
    cuttly = models.CharField(max_length=256, null=True, blank=True)