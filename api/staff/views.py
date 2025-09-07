from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.staff.models import User
from api.staff.permissions import IsManager
from api.staff.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsManager & IsAuthenticated]