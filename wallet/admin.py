from django.contrib import admin
from wallet.models.wallet import Wallet, Wallettype
# Register your models here.

admin.site.register(Wallet)
admin.site.register(Wallettype)