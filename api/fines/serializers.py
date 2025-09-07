from rest_framework import serializers

from api.fines.models import Fine
from api.pickup_points.serializers import PickupPointSerializer
from api.staff.serializers import UserSerializer


class FineSerializer(serializers.ModelSerializer):
    staff = UserSerializer(read_only=True)
    pickup_point = PickupPointSerializer(read_only=True)

    class Meta:
        model = Fine
        fields = '__all__'