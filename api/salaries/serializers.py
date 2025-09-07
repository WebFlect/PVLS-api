from rest_framework import serializers

from api.salaries.models import Salary
from api.shifts.serializers import WorkShiftSerializer
from api.staff.serializers import UserSerializer


class SalarySerializer(serializers.ModelSerializer):
    staff = UserSerializer(read_only=True)
    shift = WorkShiftSerializer(read_only=True)

    class Meta:
        model = Salary
        fields = '__all__'