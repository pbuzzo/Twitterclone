from django.db import models
from django.contrib.auth.models import AbstractUser


class TwitterUser(AbstractUser):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    notifications = models.IntegerField(default=0)
    last_checked = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    following = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=False  # follow does not go both ways, leave false
    )

    # def __str__(self):
    #     return self.username
