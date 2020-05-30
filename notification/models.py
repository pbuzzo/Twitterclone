from django.db import models
from django.utils import timezone
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from datetime import datetime, timedelta



class Notification(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet
