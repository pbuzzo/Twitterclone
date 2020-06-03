from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from notification.models import Notification
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    html = 'index.html'
    message = 'Welcome to Twitterclone!'
    if request.user.is_authenticated:
        user = TwitterUser.objects.all()
        tweets = Tweet.objects.all()
        authors = TwitterUser.objects.all()
        notifications = Notification.objects.filter(author=request.user)
        notifs_count = len(notifications)
        fols = [
            item for item in authors if item in request.user.following.all()
        ]
        follow_tweets = [
            item for item in tweets if item.author in request.user.following.all()
        ]
        return render(
            request, html, {
                "user": user,
                "follow_tweets": follow_tweets,
                "tweets": tweets,
                "notifications": notifications,
                "notifs_count": notifs_count,
                "authors": authors,
                "following": fols
            }
        )
    return render(
            request, html, {"message": message}
        )

# OLD
# @login_required
# def user_details(request, id):
#     user = TwitterUser.objects.get(id=id)
#     tweets = Tweet.objects.all()
#     return render(
#         request, "user_details.html",
#         {"user": user, "tweets": tweets}
#     )


# NEW
class UserDetails(LoginRequiredMixin, View):
    def get(self, request, id):
        user = TwitterUser.objects.get(id=id)
        tweets = Tweet.objects.all()
        return render(
            request, "user_details.html",
            {"user": user, "tweets": tweets}
        )



@login_required
def follow(request, id):
    if request.user.is_authenticated:
        to_follow = TwitterUser.objects.get(id=id)
        follower = TwitterUser.objects.get(username=request.user)
        follower.following.add(to_follow)
        follower.save()

    return HttpResponseRedirect(reverse('homepage'))


@login_required
def unfollow(request, id):
    if request.user.is_authenticated:
        to_follow = TwitterUser.objects.get(id=id)
        follower = TwitterUser.objects.get(username=request.user)
        follower.following.remove(to_follow)
        follower.save()

    return HttpResponseRedirect(reverse('homepage'))
