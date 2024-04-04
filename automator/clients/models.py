from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse

# null
# Если True, Django будет хранить пустые значения как NULL в базе данных.
# По умолчанию установлено значение False.
# blank
# Если True, поле может быть пустым. По умолчанию установлено значение False.

# Обратите внимание, что это отличается от null. null связана исключительно с базой данных,
# тогда как blank связана с проверкой. Если поле имеет blank = True, проверка формы
# позволит ввести пустое значение. Если поле имеет blank = False,
# поле будет обязательным.


# Create your models here.
class Client(models.Model):
    city = models.CharField(max_length=30, verbose_name="город")
    surname = models.CharField(
        max_length=30, verbose_name="фамилия", help_text="введите фамилию"
    )
    name = models.CharField(max_length=30, verbose_name="имя", help_text="введите имя")
    pl_birth = models.CharField(
        max_length=30, verbose_name="место рождения", help_text="введите место рождения"
    )
    birth_date = models.DateField(
        verbose_name="дата рождения", help_text="введите дату рождения"
    )
    patronymic = models.CharField(
        max_length=30, verbose_name="отчество", help_text="введите отчество"
    )
    pasp_ser = models.CharField(
        max_length=4, verbose_name="серия", help_text="введите серию паспрта"
    )
    pasp_num = models.CharField(
        max_length=6, verbose_name="номер", help_text="введите номер паспрта"
    )
    pas_home = models.CharField(
        max_length=100, verbose_name="место выдачи", help_text="введите место выдачи"
    )
    pas_date = models.DateField(
        verbose_name="дата выдачи", help_text="введите дату выдачи"
    )
    pas_code = models.CharField(
        max_length=7,
        verbose_name="код пдразделения",
        help_text="введите код пдразделения",
    )
    rigister = models.CharField(
        max_length=100, verbose_name="прописка", help_text="введите прописку"
    )
    post_index = models.CharField(
        max_length=6, verbose_name="индекс", help_text="введите индекс"
    )
    cl_inn = models.CharField(
        max_length=15, verbose_name="ИНН", help_text="введите ИНН", unique=True
    )

    cl_snils = models.CharField(
        max_length=15, verbose_name="СНИЛС", help_text="введите СНИЛС", blank=True
    )
    cl_email = models.EmailField(verbose_name="почта", help_text="введите почту")
    cl_phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True,
        verbose_name="номер",
        help_text="введите номер",
    )
    discription = models.TextField(verbose_name="заметка", null=True, blank=True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def get_absolute_url(self):
        return reverse("client", kwargs={"cl_inn": self.pk})

    class Meta:
        verbose_name = "список клиентов"
        verbose_name_plural = "список клиентов"
        ordering = ["surname", "name"]


# class lots_list_bank(models.Model):
#     client = models.ForeignKey(Client, on_delete = models.CASCADE) #  у одного клиента может быть много лотов, должна быть ссылка на Фио клиента и его номер телефона, добавь метод выше
#     lot_efrsb_urls = models.URLField(
#         max_length=200,
#         verbose_name="Сылка на ЕФРСБ",
#         help_text="Введите cылку на ЕФРСБ",
#     )
#     lot_plase_urls = models.URLField(
#         max_length=200,
#         verbose_name="Сылка на ЕФРСБ",
#         help_text="Введите cылку на ЕФРСБ",
#     )
#     obligator = models.CharField(
#         max_length=50, verbose_name="должник", help_text="Имя должнеика"
#     )
#     # proc_type = models."Помоги мне chatGPT" поле с выбором из одгого вырианта в списке [аукцион, публичное предложение] далее публичное предложение - ПП

#     end_of_feed = models.DateField(
#         verbose_name="Конец подачи заявки", help_text="веедите дату конца подачи заявки"
#     )
#     auction_day = models.DateField(
#         verbose_name="Дата проведения аукциона",
#         help_text="веедите дату проведения аукциона",
#     )
#     totl_price = models.DecimalField(
#         verbose_name="Цена лота",
#         help_text="Введите цену покупки лота, либо цену подачи на ПП",
#     )  #  по умолчанию пустое поле

#     # action_sttus = models."Помоги мне chatGPT" выбор статус таргов [проведены, не проведены,] по умолчанию пусто

#     # feed_sttus = models."Помоги мне chatGPT" выбор статуса заявки [подано, не подано,] по умолчанию пусто

#     feed_price = models.DecimalField(
#         verbose_name="введите цену заявки", help_text="введите цену за работу"
#     )
#     price_procent = models.DecimalField(
#         verbose_name="введите процент за агентское вознограждение",
#         help_text="процент за агентское вознограждение в случае победы",
#     )  # по умолчанию пустое поле
