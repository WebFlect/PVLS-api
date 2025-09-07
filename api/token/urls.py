from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.token.views import CustomTokenObtainPairView, CustomTokenVerifyView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", CustomTokenVerifyView.as_view(), name="token_verify"),
]