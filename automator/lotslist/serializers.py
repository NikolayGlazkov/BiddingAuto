from rest_framework import serializers
from .models import LotListBank

class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotListBank
        fields = ['lot_efrsb_urls']  # Указываем поля, которые хотим сериализовать
