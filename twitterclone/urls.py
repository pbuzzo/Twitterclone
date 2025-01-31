"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser.urls import urlpatterns as twitterapp_urls
from tweet.urls import urlpatterns as tweet_urls
from notification.urls import urlpatterns as notification_urls
from authentication.urls import urlpatterns as authentication_urls
import twitteruser.views

urlpatterns = [
    path('', twitteruser.views.index, name="homepage"),
    path('admin/', admin.site.urls),
]

urlpatterns += twitterapp_urls
urlpatterns += tweet_urls
urlpatterns += authentication_urls
urlpatterns += notification_urls
