from django.db import models

from api.staff.models import User


class Training(models.Model):
    trainer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trainings_given",
        verbose_name="Тренер"
    )
    trainee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="trainings_received",
        verbose_name="Обучаемый"
    )
    bonus_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Бонус за обучение"
    )

    def __str__(self):
        return f"{self.trainer} → {self.trainee} (+{self.bonus_amount} ₽)"