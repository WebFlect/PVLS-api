from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.shifts.models import WorkShift
from api.shifts.serializers import WorkShiftSerializer
from api.staff.permissions import IsManager


class WorkShiftViewSet(viewsets.ModelViewSet):
    queryset = WorkShift.objects.all()
    serializer_class = WorkShiftSerializer
    permission_classes = [IsManager & IsAuthenticated]