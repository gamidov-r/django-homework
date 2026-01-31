from django.db import models
from django.utils.module_loading import module_has_submodule


# Create your models here.
class Feedback(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Укажите заголовок")
    body = models.TextField(blank=True, null=True, verbose_name="Содержимое", help_text="Введите содржимое")
    preview = models.ImageField(
        upload_to="feedback/images",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Превью поста",
    )
    created_at = models.DateField(blank=True, null=True, verbose_name="дата создания", help_text="дата создания поста")
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    view_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите кол-во просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Записи"
        ordering = ["title", "body", "created_at", "view_counter"]

    def __str__(self):
        return self.title
