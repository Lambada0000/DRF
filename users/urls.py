from django.urls import path

from Ims.apps import ImsConfig
from users.views import UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, UserCreateAPIView

app_name = ImsConfig.name

urlpatterns = [
    path("lesson/", UserListAPIView.as_view(), name="user_list"),
    path("lesson/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("lesson/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("lesson/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("lesson/create/", UserCreateAPIView.as_view(), name="user_create"),
]
