# Generated by Django 5.0.3 on 2024-04-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_pers_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='pers_status',
            field=models.CharField(blank=True, choices=[('individual', 'Физлицо'), ('indiv_entrepr', 'ИП')], default='individual', max_length=15, verbose_name='Статус физлица'),
        ),
    ]
