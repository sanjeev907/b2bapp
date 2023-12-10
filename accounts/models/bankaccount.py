from utils.models import BaseModel
from django.db import models

class Bank(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ifsc(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class BankAccount(BaseModel):
    ACCOUNT_TYPE = (('Saving','Saving'),('Current','Current'))

    account_holser_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=100)
    confirm_account_number = models.CharField(max_length=100)
    ifsc = models.ForeignKey(Ifsc,on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100,choices=ACCOUNT_TYPE,default='Saving')
    is_active = models.BooleanField(default=True)
    is_primary = models.BooleanField(default=True)
    user = models.ForeignKey('accounts.user',on_delete=models.CASCADE)