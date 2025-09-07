from rest_framework import serializers

from api.pickup_points.serializers import PickupPointSerializer
from api.shifts.models import WorkShift
from api.staff.serializers import UserSerializer


class WorkShiftSerializer(serializers.ModelSerializer):
    staff = UserSerializer(read_only=True)
    pickup_point = PickupPointSerializer(read_only=True)
    replaced_employee = UserSerializer(read_only=True)

    class Meta:
        model = WorkShift
        fields = '__all__'