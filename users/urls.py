from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserCreateAPIView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
] + router.urls