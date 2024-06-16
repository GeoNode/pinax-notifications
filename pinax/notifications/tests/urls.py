from django.urls import re_path, include

urlpatterns = [
    re_path(r"^notifications/", include("pinax.notifications.urls", namespace="pinax_notifications")),
]
