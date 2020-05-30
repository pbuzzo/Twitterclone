from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
import re
from authentication.forms import LoginForm, CustomUserCreationForm


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data["username"],
                password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'user_form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def user_add_views(request):
    html = "user_form.html"
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tix_user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password1']
            )
            tix_user.save()
            return HttpResponseRedirect(reverse('homepage'))

    form = CustomUserCreationForm()

    return render(request, html, {'form': form})
