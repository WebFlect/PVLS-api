from rest_framework import serializers

from api.staff.serializers import UserSerializer
from api.trainings.models import Training


class TrainingSerializer(serializers.ModelSerializer):
    trainer = UserSerializer(read_only=True)
    trainee = UserSerializer(read_only=True)

    class Meta:
        model = Training
        fields = '__all__'