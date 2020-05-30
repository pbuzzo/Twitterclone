from tweet.models import Tweet
from django import forms


class TweetAddForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['title', 'date', 'description', 'author']

