from rest_framework import serializers
from .models import Pharmacy
from .models import Customer
from .models import ProductDelivery


class PharmacySerializers(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductDelivery
        fields = '__all__'