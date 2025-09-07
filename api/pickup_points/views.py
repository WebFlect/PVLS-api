from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.pickup_points.models import PickupPoint
from api.pickup_points.serializers import PickupPointSerializer
from api.staff.permissions import IsManager


class PickupPointViewSet(viewsets.ModelViewSet):
    queryset = PickupPoint.objects.all()
    serializer_class = PickupPointSerializer
    permission_classes = [IsManager & IsAuthenticated]