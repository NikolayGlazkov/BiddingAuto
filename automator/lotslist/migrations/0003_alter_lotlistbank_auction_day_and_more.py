# Generated by Django 5.0.3 on 2024-04-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotslist', '0002_alter_lotlistbank_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotlistbank',
            name='auction_day',
            field=models.DateTimeField(verbose_name='Дата проведения аукциона'),
        ),
        migrations.AlterField(
            model_name='lotlistbank',
            name='end_of_feed',
            field=models.DateTimeField(verbose_name='Конец подачи заявки'),
        ),
    ]
