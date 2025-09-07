from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.trainings.models import Training
from api.trainings.serializers import TrainingSerializer
from api.staff.permissions import IsManager


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    permission_classes = [IsManager & IsAuthenticated]