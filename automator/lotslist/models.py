from django.db import models
from clients.models import Client

class LotListBank(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    lot_efrsb_urls = models.URLField(max_length=200, verbose_name="Ссылка на ЕФРСБ", help_text="Введите ссылку на ЕФРСБ")
    lot_place_urls = models.URLField(max_length=200, verbose_name="Ссылка на местопровеления торга", help_text="Введите ссылку на местоположение лота")
    obligator = models.CharField(max_length=50, verbose_name="Должник", help_text="Имя должника")

    PROCEDURE_TYPE_CHOICES = [
        ('auction', 'Аукцион'),
        ('public_offer', 'Публичное предложение'),
    ]
    proc_type = models.CharField(max_length=20, choices=PROCEDURE_TYPE_CHOICES, verbose_name="Тип процедуры")

    end_of_feed = models.DateTimeField(verbose_name="Конец подачи заявки")
    auction_day = models.DateTimeField(verbose_name="Дата проведения аукциона")
    total_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена лота", blank=True, null=True)

    ACTION_STATUS_CHOICES = [
        ('conducted', 'Проведены'),
        ('not_conducted', 'Не проведены'),
    ]
    action_status = models.CharField(max_length=15, choices=ACTION_STATUS_CHOICES, verbose_name="Статус торгов", blank=True, null=True)

    APPLICATION_STATUS_CHOICES = [
        ('submitted', 'Подано'),
        ('not_submitted', 'Не подано'),
    ]
    feed_status = models.CharField(max_length=13, choices=APPLICATION_STATUS_CHOICES, verbose_name="Статус заявки", blank=True, null=True)

    feed_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена заявки")
    price_procent = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Процент за агентское вознаграждение", blank=True, null=True)

    def __str__(self):
        return f"Лот {self.id} - Клиент {self.client.full_name}"

    class Meta:
        verbose_name = "лоты"
        verbose_name_plural = "Список лотов"