from django.urls import path
from tweet import views

urlpatterns = [
    path('tweet/<int:id>/', views.tweet_details, name="tweet_details"),
    path('tweetadd/', views.tweet_add_views, name="tweet_add_view"),
]
