from django.db import models
from django.utils.module_loading import module_has_submodule

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категория", help_text="Категория с продуктами")
    description = models.CharField(
        blank=True, null=True, verbose_name="Описание", help_text="Описание категории с продуктами"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Продукт", help_text="Наименование Продукта")
    description = models.CharField(blank=True, null=True, verbose_name="Описание", help_text="Описание Продукта")
    img = models.ImageField(
        upload_to="products/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Изображение продукта",
    )
    # category = models.CharField(max_length=100, verbose_name="Продукт", help_text="Наименование Продукта")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Категория продукта",
        null=True,
        blank=True,
        related_name="products",
    )
    value = models.IntegerField()
    created_at = models.DateField(
        blank=True, null=True, verbose_name="дата создания", help_text="дата создания продукта"
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="дата изменения", help_text="дата последнего изменения продукта"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "created_at", "updated_at", "value"]

    def __str__(self):
        return self.name



