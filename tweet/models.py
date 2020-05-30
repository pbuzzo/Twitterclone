from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser


class Tweet(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.title
