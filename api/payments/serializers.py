from rest_framework import serializers

from api.payments.models import Payment
from api.staff.models import User
from api.staff.serializers import UserSerializer


class PaymentSerializer(serializers.ModelSerializer):
    staff = UserSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'