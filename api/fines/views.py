from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.fines.models import Fine
from api.fines.serializers import FineSerializer
from api.staff.permissions import IsManager


class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    permission_classes = [IsManager & IsAuthenticated]