from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

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
    pl_birth = models.CharField(max_length=30, verbose_name="место рождения", help_text="введите место рождения")
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
