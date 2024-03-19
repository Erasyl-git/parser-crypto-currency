from django.contrib import admin
from .models import CryptoCurrency

class CryptoAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'change']

    def get_name(self, obj):
        return obj.name
    
    def get_price(self, obj):
        return obj.price

    def get_change(self, obj):
        return obj.change

admin.site.register(CryptoCurrency, CryptoAdmin)

