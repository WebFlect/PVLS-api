from django.db import models

from api.pickup_points.models import PickupPoint
from api.staff.models import User


class Fine(models.Model):
    STATUS_CHOICES = [
        ('counted', 'Учитывается'),
        ('disputed', 'Оспорен'),
        ('pending', 'На проверке'),
    ]
    date_time = models.DateTimeField(verbose_name="Дата и время штрафа")
    reason = models.TextField(verbose_name="Причина")
    claim_number = models.CharField(max_length=50, verbose_name="Номер претензии")
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE, verbose_name="Пункт выдачи")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма штрафа")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")
    staff = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Сотрудник", related_name="penalties")

    def __str__(self):
        return f"{self.claim_number} - {self.staff}"