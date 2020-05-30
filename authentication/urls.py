from django.urls import path
from authentication import views

urlpatterns = [
    path('useradd/', views.user_add_views, name="user_add_view"),
    path('login/', views.loginview, name="login"),
    path('logout/', views.logoutview, name="logout"),
]
