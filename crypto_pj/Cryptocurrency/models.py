from django.db import models


class CryptoCurrency(models.Model):

    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=15, decimal_places=3)
    volume = models.DecimalField(max_digits=15, decimal_places=3)  # Объем торгов
    change = models.DecimalField(max_digits=15, decimal_places=3)  # Изменение цены за последний период времени
    last_updated = models.DateTimeField(auto_now=True)  # Дата и время обновления данных
    

    def __str__(self):
        return f'{self.name}|{self.currency}'
    
    