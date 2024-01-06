from rest_framework import serializers
from wallet.models.wallet import Wallet, Wallettype

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'