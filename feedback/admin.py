from django.contrib import admin
from feedback.models import Feedback

# Register your models here.


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "body", "preview", "created_at", "published", "view_counter")
    search_fields = (
        "title",
        "body",
    )
