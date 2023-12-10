from rest_framework import serializers
from accounts.models.address import *


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        models = Zone
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        models = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        models = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        models = State
        fields = '__all__'

class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Pincode
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        models = Address
        fields = '__all__'