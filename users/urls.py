from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import (
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
    UserCreateAPIView,
    PaymentsViewSet,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"payment", PaymentsViewSet, basename="payment")

urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_delete"),
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
