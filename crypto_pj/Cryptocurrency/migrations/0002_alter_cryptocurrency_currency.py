# Generated by Django 5.0.1 on 2024-03-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cryptocurrency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='currency',
            field=models.CharField(max_length=4),
        ),
    ]
