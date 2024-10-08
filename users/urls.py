from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from Ims.views import SubscriptionAPIView, SubscriptionListAPIView
from users.apps import UsersConfig
from users.views import (PaymentsViewSet, UserCreateAPIView,
                         UserDestroyAPIView, UserListAPIView,
                         UserRetrieveAPIView, UserUpdateAPIView, PaymentsCreateAPIView)

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"user/payment", PaymentsViewSet, basename="payment")

urlpatterns = [
    path("user/", UserListAPIView.as_view(), name="user_list"),
    path("user/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("user/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("user/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
    path(
        "register/",
        UserCreateAPIView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path(
        "subs/create/",
        SubscriptionAPIView.as_view(),
        name="subscription_create",
    ),
    path("subs/", SubscriptionListAPIView.as_view(), name="subscription_list"),
    path("payment/", PaymentsCreateAPIView.as_view(), name="payment"),
]

urlpatterns += router.urls
