from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.salaries.models import Salary
from api.salaries.serializers import SalarySerializer
from api.staff.permissions import IsManager


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    permission_classes = [IsManager & IsAuthenticated]