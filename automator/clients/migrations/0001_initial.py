# Generated by Django 5.0.3 on 2024-03-20 15:50

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='город')),
                ('surname', models.CharField(help_text='введите фамилию', max_length=30, verbose_name='фамилия')),
                ('name', models.CharField(help_text='введите имя', max_length=30, verbose_name='имя')),
                ('pl_birth', models.CharField(help_text='введите место рождения', max_length=30, verbose_name='место рождения')),
                ('birth_date', models.DateField(help_text='введите дату рождения', verbose_name='дата рождения')),
                ('patronymic', models.CharField(help_text='введите отчество', max_length=30, verbose_name='отчество')),
                ('pasp_ser', models.CharField(help_text='введите серию паспрта', max_length=4, verbose_name='серия')),
                ('pasp_num', models.CharField(help_text='введите номер паспрта', max_length=6, verbose_name='номер')),
                ('pas_home', models.CharField(help_text='введите место выдачи', max_length=100, verbose_name='место выдачи')),
                ('pas_date', models.DateField(help_text='введите дату выдачи', verbose_name='дата выдачи')),
                ('pas_code', models.CharField(help_text='введите код пдразделения', max_length=7, verbose_name='код пдразделения')),
                ('rigister', models.CharField(help_text='введите прописку', max_length=100, verbose_name='прописка')),
                ('post_index', models.CharField(help_text='введите индекс', max_length=6, verbose_name='индекс')),
                ('cl_inn', models.CharField(help_text='введите ИНН', max_length=15, unique=True, verbose_name='ИНН')),
                ('cl_snils', models.CharField(blank=True, help_text='введите СНИЛС', max_length=15, verbose_name='СНИЛС')),
                ('cl_email', models.EmailField(help_text='введите почту', max_length=254, verbose_name='почта')),
                ('cl_phone', phonenumber_field.modelfields.PhoneNumberField(help_text='введите номер', max_length=128, region=None, unique=True, verbose_name='номер')),
                ('discription', models.TextField(blank=True, null=True, verbose_name='заметка')),
            ],
        ),
    ]
