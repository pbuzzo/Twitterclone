from django.urls import path
from twitteruser import views

urlpatterns = [
    path('user/<int:id>/', views.UserDetails.as_view(), name="user_details"),
    path('follow/<int:id>/', views.follow, name="follow"),
    path('unfollow/<int:id>/', views.unfollow, name="unfollow"),
]
