from django.forms import ModelForm, BooleanField
from django.utils import timezone

from catalog.models import Product
from django.core.exceptions import ValidationError

blacklist_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class StyleFormProduct:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("view_counter",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"

    def clean_name(self):
        name = self.cleaned_data["name"].lower()
        for word in blacklist_words:
            if word in name:
                raise ValidationError("Недопустимое название продукта")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"].lower()
        for word in blacklist_words:
            if word in description:
                raise ValidationError("Недопустимые слова в описании")
        return description

    def clean_value(self):
        value = self.cleaned_data["value"]
        if value < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return value

    def clean_created_at(self):
        created_at = self.cleaned_data["created_at"]
        current = timezone.now().date()
        if not created_at == None:
            if created_at > current:
                raise ValidationError("Дата создания не может быть позднее текущей даты")
        return created_at

    def clean_updated_at(self):
        updated_at = self.cleaned_data["updated_at"]
        created_at = self.cleaned_data["created_at"]
        if not updated_at == None:
            if updated_at < created_at:
                raise ValidationError("Дата обновления продукта не может быть раньше даты создания")
        return updated_at

    def clean_img(self):
        img = self.cleaned_data["img"]
        if img == None:
            return img
        size = img.size
        limit = 5 * 1024 * 1024  # 5 MB
        if size > limit:
            raise ValidationError("Превышен лимит размера файла в 5 MB")
        if img.format not in ["JPEG", "PNG"]:
            raise ValidationError("Формат изображения не является JPEG или PNG")
        return img


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ("published",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"

    def clean_name(self):
        name = self.cleaned_data["name"].lower()
        for word in blacklist_words:
            if word in name:
                raise ValidationError("Недопустимое название продукта")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"].lower()
        for word in blacklist_words:
            if word in description:
                raise ValidationError("Недопустимые слова в описании")
        return description

    def clean_value(self):
        value = self.cleaned_data["value"]
        if value < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return value

    def clean_created_at(self):
        created_at = self.cleaned_data["created_at"]
        current = timezone.now().date()
        if not created_at == None:
            if created_at > current:
                raise ValidationError("Дата создания не может быть позднее текущей даты")
        return created_at

    def clean_updated_at(self):
        updated_at = self.cleaned_data["updated_at"]
        created_at = self.cleaned_data["created_at"]
        if not updated_at == None:
            if updated_at < created_at:
                raise ValidationError("Дата обновления продукта не может быть раньше даты создания")
        return updated_at

    def clean_img(self):
        img = self.cleaned_data["img"]
        if img == None:
            return img
        size = img.size
        limit = 5 * 1024 * 1024  # 5 MB
        if size > limit:
            raise ValidationError("Превышен лимит размера файла в 5 MB")
        if img.format not in ["JPEG", "PNG"]:
            raise ValidationError("Формат изображения не является JPEG или PNG")
        return img
