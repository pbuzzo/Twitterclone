from django import forms
from twitteruser.models import TwitterUser
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = TwitterUser
        fields = ('username', 'name', 'bio', 'password1', 'password2')
