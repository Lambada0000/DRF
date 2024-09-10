from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Ims/course/", include("Ims.urls", namespace="Ims")),
    path("Ims/", include("users.urls", namespace="user")),
]
