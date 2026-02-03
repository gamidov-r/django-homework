from django.contrib.auth.models import AbstractUser#, User
from django.db import models
from django.db.models import ForeignKey
from django.conf import settings
#from catalog.models import Product


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=20, verbose_name="Телефон", blank=True, null=True, help_text="Введите номер телефона"
    )
    country = models.CharField(max_length=20, verbose_name="Страна", blank=True, null=True, help_text="Страна")
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", null=True, blank=True, help_text="Фото профиля"
    )
    # owner = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner = models.ForeignKey('self', on_delete=models.CASCADE, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
