from rest_framework import serializers
from accounts.models.address import *


class ZoneSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name':'name is required'})
    

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name':'name is required'})

class StateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name':'name is required'})
    
class CitySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name':'name is required'})

class PincodeSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name':'name is required'})

class AddressSerializer(serializers.Serializer):
    address_tye = serializers.CharField(required=True, error_messages = {'address_tye':'address_tye is required'})
    street_address = serializers.CharField(required=True, error_messages = {'street_address':'street_address is required'})
    landmark = serializers.CharField(required=True, error_messages = {'landmark':'landmark is required'})
    locality = serializers.CharField(required=True, error_messages = {'locality':'locality is required'})
    # state = serializers.CharField(required=False)
    # city = serializers.CharField(required=False)