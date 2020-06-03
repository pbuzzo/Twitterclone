from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

# OLD
# @login_required
# def notification_views(request, id):
#     if request.user.is_authenticated:
#         html = 'notifications.html'
#         author = TwitterUser.objects.get(id=id)
#         notifications = Notification.objects.filter(author=request.user)
#         copy_tweets = [tweet for tweet in notifications]
#         Notification.objects.filter(author=request.user).delete()

#         return render(
#             request,
#             html,
#             {"author": author, "notifications": copy_tweets}
#         )
#     return HttpResponseRedirect(reverse("login"))


# NEW
class NotificationView(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_authenticated:
            html = 'notifications.html'
            author = TwitterUser.objects.get(id=id)
            notifications = Notification.objects.filter(author=request.user)
            copy_tweets = [tweet for tweet in notifications]
            Notification.objects.filter(author=request.user).delete()

            return render(
                request,
                html,
                {"author": author, "notifications": copy_tweets}
            )
        return HttpResponseRedirect(reverse("login"))
