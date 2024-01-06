from django.db import models
from utils.models import BaseModel
from tinymce.models import HTMLField
from wallet.models.wallet import *



class Category(BaseModel):
    slug = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'category/')
    is_active = models.BooleanField(default=True)

class SubCategory(BaseModel):
    slug = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'sub-category/')
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ProductFile(BaseModel):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to = 'productFile/')
    is_active = models.BooleanField(default=True)

class Product(BaseModel):
    name = models.CharField(max_length=255)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    points = models.PositiveIntegerField(null=True,blank=True)
    t_c = models.TextField(null=True, blank=True)
    image = models.ManyToManyField(ProductFile, blank=True)
    category = models.ManyToManyField(Category, related_name='product',null=True,blank=True)
    subcategory = models.ManyToManyField(SubCategory,related_name='product',null=True,blank=True )
    video = models.FileField(upload_to = 'product-video/', blank=True, null=True)
    varients = models.ManyToManyField('self', blank=True)
    complimentary_products = models.ManyToManyField('self', blank=True)
    inclusion = HTMLField(blank=True,null = True, max_length=4096)
    wallet = models.ManyToManyField(Wallettype, blank=True, null=True)
