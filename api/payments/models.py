import datetime

from django.db import models

from api.staff.models import User


class Payment(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    date = models.DateField(default=datetime.date.today, verbose_name="Дата выплаты")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    is_paid = models.BooleanField(default=False, verbose_name="Выплачено")
    delay_reason = models.TextField(null=True, blank=True, verbose_name="Причина задержки")

    def __str__(self):
        return f"{self.staff} - {self.amount} ({'Выплачено' if self.is_paid else 'Не выплачено'})"