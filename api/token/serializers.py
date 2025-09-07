from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from api.staff.serializers import UserSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # можем добавить кастомные поля в payload
        token["phone"] = user.phone
        token["is_manager"] = user.is_manager
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            "user": UserSerializer(self.user).data
        })
        return data