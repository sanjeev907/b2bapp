from rest_framework import serializers
from accounts.models.bankaccount import *

class BankSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})
    

class IfscSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})
    address = serializers.CharField(required=True, error_messages = {'address': 'address is required'})


class BankAccountSerializer(serializers.Serializer):
    ifsc = serializers.CharField(required=True, error_messages ={'ifsc': 'ifsc is required'})
    account_holder_name = serializers.CharField(required=True, error_messages = {'name': 'name is required'})
    account_number = serializers.CharField(required=True, error_messages = {'account_number': 'account_number is required'})
    confirm_account_number = serializers.CharField(required=True, error_messages = {'confirm_account_number': 'confirm_account_number is required'})
    account_type = serializers.CharField(required=True, error_messages = {'account_type': 'account_type is required'})