from django.db import models
from apps.user.enums import GENDER, RoleOptions
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# you could extend, modify the original User class given by Django
class User(AbstractUser):
    first_name = None  # remove this field
    last_name = None  # remove this field
    username = models.CharField(max_length=100, null=False, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"user {self.username}"

    class Meta:
        # app_name_model_name, user_user
        db_table = "user"


# One-to-One relationship


class Profile(models.Model):
    # user = models.ForeignKey("user.User", on_delete = models.CASCADE, unique = True)
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        unique=True,
    )
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
