from django.urls import path

from apps.core.api.viewsets import ConverterView

urlpatterns = [path("converter", ConverterView.as_view(), name="converter")]
