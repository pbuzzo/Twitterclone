from django.urls import path
from tweet import views

urlpatterns = [
    path('tweet/<int:id>/', views.TweetDetails.as_view(), name="tweet_details"),
    path('tweetadd/', views.AddTweet.as_view(), name="tweet_add_view"),
]
