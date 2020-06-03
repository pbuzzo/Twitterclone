from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from tweet.forms import TweetAddForm
from twitteruser.models import TwitterUser
from notification.models import Notification
import re
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# OLD
# @login_required
# def tweet_details(request, id):
#     tweet = Tweet.objects.get(id=id)
#     return render(request, "tweet_details.html", {"tweet": tweet})

# NEW
class TweetDetails(LoginRequiredMixin, View):
    def get(self, request, id):
        tweet = Tweet.objects.get(id=id)
        return render(request, "tweet_details.html", {"tweet": tweet})


# # OLD
# @login_required
# def tweet_add_views(request):
#     html = "tweet_form.html"

#     # POST request
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = TweetAddForm(request.POST)
#             authors = TwitterUser.objects.all()
#             if form.is_valid():
#                 data = form.cleaned_data
#                 Tweet.objects.create(
#                     title=data['title'],
#                     date=data['date'],
#                     author=data['author'],
#                     description=data['description'],
#                 )
#                 for item in authors:
#                     if re.search("@" + str(item), data['description']):
#                         marked = TwitterUser.objects.get(username=item)
#                         marked.notifications += 1
#                         marked.save()
#                         Notification.objects.create(
#                             tweet=Tweet.objects.get(title=data['title']),
#                             author=marked,
#                         )
#                 return HttpResponseRedirect(reverse("homepage"))

#     form = TweetAddForm()

#     return render(request, html, {'form': form})


# NEW
class AddTweet(LoginRequiredMixin, View):
    def get(self, request):
        html = 'tweet_form.html'
        form = TweetAddForm()
        return render(request, html, {'form': form})
    def post(self, request):
        form = TweetAddForm(request.POST)
        authors = TwitterUser.objects.all()
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                title=data['title'],
                date=data['date'],
                author=data['author'],
                description=data['description'],
            )
        for item in authors:
            if re.search("@" + str(item), data['description']):
                marked = TwitterUser.objects.get(username=item)
                marked.notifications += 1
                marked.save()
                Notification.objects.create(
                    tweet=Tweet.objects.get(title=data['title']),
                    author=marked,
                )
        return HttpResponseRedirect(reverse("homepage"))