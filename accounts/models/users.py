from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager , PermissionsMixin, Group, Permission


class CustomManager(BaseUserManager):
    def create_user(self, email, mobile_number, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if mobile_number is None:
            raise ValueError('Users must have an mobile number')
        email = self.normalize_email(email)
        user = self.model(email=email,mobile_number = mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, mobile_number, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, mobile_number, password, **extra_fields)



LOGIN_TYPE  = (('email', 'email'),('mobile','mobile'))

class User(AbstractUser, PermissionsMixin):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(null=True,blank=True, unique= True)
    mobile_number = models.CharField(max_length=13,unique=True)
    date_joined = models.DateField(default=timezone.now)
    otp = models.CharField(max_length=6,blank=True)
    login_type = models.CharField(max_length=10,choices= LOGIN_TYPE, default='email')
    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_number']

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, help_text='The groups this user belongs to.', related_name='user_groups_accounts')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_permissions_accounts')



    def __str__(self):
        return self.email