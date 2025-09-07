from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.payments.models import Payment
from api.payments.serializers import PaymentSerializer
from api.staff.permissions import IsManager


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsManager & IsAuthenticated]