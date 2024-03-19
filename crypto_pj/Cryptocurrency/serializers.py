from rest_framework import serializers
from .models import CryptoCurrency


class CryptoCurrencySerizliser(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = '__all__'
