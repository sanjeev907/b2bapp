from utils.models import BaseModel
from django.db import models
from accounts.models.users import User
from django.core.validators import RegexValidator


class Hobby(BaseModel):
    name = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name

class Interest(BaseModel):
    name = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name


class UserType(BaseModel):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

aadhr_card_validator = RegexValidator(regex = r'^\d{12}$',message="aadhar number must be a 12 digit numberic value")

class UserProfile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_parents = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True,related_name='user_profile_parents')
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE,null=True, blank= True)
    dealer_code = models.CharField(max_length=100, unique=True, null= True, blank=True)
    name =  models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    alternate_mobile = models.CharField(max_length=10, null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    aadhar_card = models.CharField(max_length=12, validators=[aadhr_card_validator])
    aadhar_front_image = models.ImageField(upload_to='aadhar_images/')
    aadhar_back_image = models.ImageField(upload_to='aadhar_images/') 
    have_kids = models.BooleanField(default=True)
    no_of_kids = models.BooleanField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_married = models.BooleanField(default=False)
    have_parents = models.BooleanField(default= True)
    interest = models.ManyToManyField(Interest,blank=True)
    hobby = models.ManyToManyField(Hobby,blank=True)

    def __str__(self) -> str:
        return self.user.mobile_number
    

COMPANY_TYPE= (('Private Limited Company','Private Limited Company'),
               ('Public Company', 'Public Company'),('Sole Proprietorship','Sole Proprietorship'),
               ('One Person Company','One Person Company'),('Partership','Partership'),('LLP','LLP'),)


pan_number_validator = RegexValidator(
    regex=r'^[A-Za-z]{5}\d{4}[A-Za-z]{1}$',
    message="Enter a valid PAN number."
)

gst_number_validator = RegexValidator(
    regex=r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}\d[Z]{1}[A-Z\d]{1}$',
    message="Enter a valid GST number."
)

class  Company(BaseModel):
    name = models.CharField(max_length=255)
    comapny_type = models.CharField(max_length=255, choices= COMPANY_TYPE)
    firm_image= models.ImageField(upload_to = 'firm_images/')
    pan_number = models.CharField(max_length= 10, validators=[pan_number_validator]) 
    gst_in = models.CharField(max_length=15, validators=[gst_number_validator]) 
    gst_image = models.ImageField(upload_to = 'gst_images/') 
    user =  models.ForeignKey(User,on_delete= models.CASCADE)  # type: ignore
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name
    


