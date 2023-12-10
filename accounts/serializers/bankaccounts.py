from rest_framework import serializers
from accounts.models.bankaccount import *

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        models = Bank
        fields = '__all__'

class IfscSerializer(serializers.ModelSerializer):
    class Meta:
        models = Ifsc
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        models = BankAccount
        fields = '__all__'