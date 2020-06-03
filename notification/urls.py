from django.urls import path
from notification import views

urlpatterns = [
    path(
        'notifications/<int:id>/',
        views.NotificationView.as_view(),
        name="notification_view"
    ),
]
