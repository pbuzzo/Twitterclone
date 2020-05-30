from django.urls import path
from twitteruser import views

urlpatterns = [
    path('user/<int:id>/', views.user_details, name="user_details"),
    path('follow/<int:id>/', views.follow, name="follow"),
    path('unfollow/<int:id>/', views.unfollow, name="unfollow"),
]
