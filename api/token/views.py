from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework.response import Response
from rest_framework import status
from api.staff.models import User
from jwt import decode as jwt_decode
from django.conf import settings
from jwt import InvalidTokenError

from api.staff.serializers import UserSerializer
from api.token.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenVerifyView(TokenVerifyView):
    serializer_class = TokenVerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            token = request.data.get("token")
            payload = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])

            return Response({ "user": UserSerializer(user).data }, status=status.HTTP_200_OK)

        except InvalidTokenError:
            return Response({"valid": False}, status=status.HTTP_401_UNAUTHORIZED)