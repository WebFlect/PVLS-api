from datetime import datetime
from django.db.models.functions import Now

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        login = username
        if not login:
            login = f"user{datetime.now().strftime('%d%m%H%M%S')}"
        user = self.model(username=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_manager(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_manager", True)
        return self.create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self.create_manager(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=250, unique=True, verbose_name="Логин")
    phone = models.CharField(max_length=20, unique=True, verbose_name="Телефон")
    email = models.EmailField(unique=True, verbose_name="Email")

    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    date_joined_work = models.DateField(default=Now(), verbose_name="Дата зачисления на работу")
    date_contract_end = models.DateField(null=True, blank=True, verbose_name="Дата завершения контракта (факт)")

    bank_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Банк")
    cash_payment = models.BooleanField(default=False, verbose_name="Выплата наличными")

    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, null=True, blank=True, verbose_name="Отчество")

    # менеджеры
    is_manager = models.BooleanField(default=False, verbose_name="Менеджер")
    position_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # обязательные для AbstractBaseUser
    is_superuser = models.BooleanField(default=False)  # только для админки
    is_active = models.BooleanField(default=True)     # чтобы JWT работал

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"