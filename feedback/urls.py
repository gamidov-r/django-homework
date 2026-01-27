from django.urls import path
from feedback.apps import FeedbackConfig

from feedback.views import FeedbackListView, FeedbackDetailView, FeedbackCreateView, FeedbackUpdateView, FeedbackDeleteView

app_name = FeedbackConfig.name

urlpatterns = [
    path("", FeedbackListView.as_view(), name="entity_list"),
    path("feedback/<int:pk>/", FeedbackDetailView.as_view(), name="entity_detail"),
    path("feedback/create", FeedbackCreateView.as_view(), name="entity_create"),
    path("feedback/<int:pk>/update/", FeedbackUpdateView.as_view(), name="entity_update"),
    path("feedback/<int:pk>/delete/", FeedbackDeleteView.as_view(), name="entity_delete"),
]
