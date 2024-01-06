from django.db import models
from utils.models import BaseModel
from accounts.models.users import User


class Wallettype(BaseModel):
    name = models.CharField(max_length = 255, unique = True)
    
    def __str__(self):
        return self.name
    
class Wallet(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_type = models.ForeignKey(Wallettype, on_delete=models.CASCADE, null= True, blank = True)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default = 0.00)# type: ignore #
    is_active = models.BooleanField(default = True)
    is_default = models.BooleanField(default = False)

    def __str__(self):
        return self.user.mobile_number
