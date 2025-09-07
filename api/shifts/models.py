from django.db import models

from api.pickup_points.models import PickupPoint
from api.staff.models import User


class WorkShift(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shifts", verbose_name="Сотрудник")
    pickup_point = models.ForeignKey(PickupPoint, on_delete=models.CASCADE, verbose_name="Пункт выдачи")
    replaced_employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="replaced_shifts", verbose_name="Замененный сотрудник")
    date = models.DateField(verbose_name="Дата работы")
    start_time = models.TimeField(verbose_name="Время начала работы")
    end_time = models.TimeField(verbose_name="Время окончания работы")

    def __str__(self):
        return f"{self.date} - {self.staff} @ {self.pickup_point}"