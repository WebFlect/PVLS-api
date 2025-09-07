from django.db import models

class PickupPoint(models.Model):
    TYPE_CHOICES = [
        ('ozon', 'Ozon'),
        ('wildberries', 'Wildberries'),
        ('yandex', 'Яндекс.Маркет'),
        ('other', 'Другое'),
    ]
    name = models.CharField(max_length=100, verbose_name="Название пункта")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Тип пункта")

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"