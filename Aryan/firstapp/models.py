from typing import Sequence
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey
from django.core.validators import RegexValidator


# Create your models here.
class Database(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)

class countries(models.Model):
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.country
class gemtype(models.Model):
    gem = models.CharField(max_length=50)
    def __str__(self):
        return self.gem

class companyinfo(models.Model):
      date = models.DateField(auto_now_add=True)
      company_name = models.CharField(max_length=100)
      contact = models.CharField(max_length=20)
      address = models.TextField()
      country = models.ForeignKey('countries',on_delete=models.PROTECT)
      mobile_no = models.CharField(max_length=20)
      tel_no = models.CharField(max_length=20,null=True)
      email = models.EmailField()
      website = models.EmailField(max_length=150,null=True,blank=True)
      pan_no = models.CharField(max_length=20)
      GST_no = models.CharField(max_length=20)
      line_id = models.CharField(max_length=20,null=True,blank=True)
      wechat_id = models.CharField(max_length=50,null=True,blank=True)
      def __str__(self):
        return self.company_name
    

class loc(models.Model):
    place=models.CharField(max_length=30)
    def __str__(self):
        return self.place
class jewell(models.Model):
    jewel=models.CharField(max_length=30)
    def __str__(self):
        return self.jewel
class centerstone(models.Model):
    stone=models.CharField(max_length=30)
    def __str__(self):
        return self.stone
class colorofcstone(models.Model):
    color=models.CharField(max_length=30)
    def __str__(self):
        return self.color
class shape1(models.Model):
    shape=models.CharField(max_length=30)
    def __str__(self):
        return self.shape
class metal1(models.Model):
    metal=models.CharField(max_length=30)
    def __str__(self):
        return self.metal
class certificate(models.Model):
    cert=models.CharField(max_length=30)
    def __str__(self):
        return self.cert
class Currency(models.Model):
    country=models.ForeignKey(countries,on_delete=models.PROTECT)
    curr=models.CharField(max_length=10)
    def __str__(self):
        return self.curr

class POJ(models.Model):

    date = models.DateField(auto_now_add=True)
    stockid = models.CharField(max_length=30,blank=True)
    company_name = models.ForeignKey('companyinfo', on_delete=PROTECT)
    location = models.ForeignKey('loc', on_delete=models.PROTECT, null=True)
    jewellery = models.ForeignKey('jewell', on_delete=models.PROTECT, null=True)
    center_stone = models.ForeignKey('centerstone', on_delete=models.PROTECT, null=True)
    color_of_center_stone = models.ForeignKey('colorofcstone', on_delete=models.PROTECT, null=True)
    shape = models.ForeignKey('shape1', on_delete=models.PROTECT, null=True, blank=True)
    metal = models.ForeignKey('metal1', on_delete=models.PROTECT, null=True)
    grosswt = models.BigIntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    cert = models.ForeignKey('certificate', on_delete=models.PROTECT, null=True)
    pieces = models.BigIntegerField()
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    discount_amount = models.DecimalField(decimal_places=2, max_digits=9, blank=True, null=True)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):

        self.discount_amount = (self.amount * self.discount) // 100
        self.stockid=str(str('S-')+str(self.id))
        super(POJ, self).save(*args, **kwargs)
    # amount=models.FloatField()
    # discount= models.FloatField(blank=True, default=0)
    # discount_amount=models.FloatField('get_discount()',blank=True, default=0)
    # total_val_j=models.FloatField('get_total_price()',default=0)
    currency=models.ForeignKey('Currency',on_delete=models.PROTECT)
    tag_price = models.BigIntegerField()
    rate = models.IntegerField()
    def __str__(self):
        return self.id


