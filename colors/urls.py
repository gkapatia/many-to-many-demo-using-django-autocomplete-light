from django.urls import path

from colors.views import ColorAutocomplete

urlpatterns = [
    path('color-autocomplete/', ColorAutocomplete.as_view(), name='color-autocomplete'),
]
