from utils.models import BaseModel
from django.db import models
from accounts.models.users import User

class Spouse(BaseModel):
    name = models.CharField(max_length=255,null=True, blank=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    dob = models.DateField()
    doa = models.DateField()
    profession = models.CharField(max_length=255, null=True, blank=True)
    mobile =  models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=15, null=True, blank=True)

class Parents(BaseModel):
    PARENTS_CHOICE = (('Mother', 'Mother'),('Father', 'Father'))

    name = models.CharField(max_length=255,null=True, blank= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    parent = models.CharField(max_length=150,choices=PARENTS_CHOICE,default='Father')
    dob = models.DateField()


class Kids(BaseModel):
    KIDS_TYPE= (('Male', 'Male'),('Female', 'Female'))

    name = models.CharField(max_length=255,null=True, blank= True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=255)