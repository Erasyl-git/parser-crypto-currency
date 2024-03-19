from django.urls import path
from .views import CryptocurrencyAPIview

urlpatterns = [
    path('currency/', CryptocurrencyAPIview.as_view(), name='currency')
]
