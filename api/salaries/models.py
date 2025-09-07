from django.db import models

from api.shifts.models import WorkShift
from api.staff.models import User


class Salary(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name="salaries")
    shift = models.ForeignKey(WorkShift, on_delete=models.CASCADE, related_name="salaries", null=True, blank=True)

    base_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Базовая ставка")
    bonus_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Надбавка")

    created_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.base_amount + self.bonus_amount

    def __str__(self):
        return f"{self.staff} - {self.total()}"