from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Ims/", include("Ims.urls", namespace="Ims")),
    path("user/", include("users.urls", namespace="user")),
]
