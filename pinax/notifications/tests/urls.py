from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path(r"^notifications/", include("pinax.notifications.urls", namespace="pinax_notifications")),
]
