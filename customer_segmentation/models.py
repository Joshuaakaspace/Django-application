from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Accounts1(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Cancelled', 'Cancelled'),
    )
    a_number = models.CharField(max_length=20,primary_key="true")
    account_name = models.CharField(max_length=50, null=True, blank=True, default="")
    account_status= models.CharField(max_length=40, choices=STATUS, null=True, blank=True, default="")
    address = models.CharField(max_length=300, null=True, blank=True, default="")
    country = models.CharField(max_length=50, null=True, blank=True, default="")
    exit_rate = models.IntegerField(null=True, blank=True, default=0)
    exit_rate_usd = models.IntegerField(null=True, blank=True, default=0)
    oppertunity_type = models.IntegerField(null=True, blank=True, default=0)
    ultimate_parent = models.CharField(max_length=50, null=True, blank=True, default=None)
    sfdc_segmentation = models.CharField(max_length=300, null=True, blank=True, default="")
    org_type_1 = models.CharField(max_length=50, null=True, blank=True, default=None)
    org_type_2 = models.CharField(max_length=50, null=True, blank=True, default=None)
    org_type_3 = models.CharField(max_length=50, null=True, blank=True, default=None)
    org_type_4 = models.CharField(max_length=300, null=True, blank=True, default=None)
    org_type_5 = models.CharField(max_length=300, null=True, blank=True, default=None)
    last_updated = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    segment_source = models.CharField(max_length=300, null=True, blank=True, default=None)
    entity_url = models.CharField(max_length=300, null=True, blank=True, default=None)
    unavailable = models.CharField(max_length=300, null=True, blank=True, default="")
    modified = models.DateTimeField(verbose_name='date_modified', auto_now=True)
    
    def __str__(self):
        return self.a_number

class Accounts2(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Cancelled', 'Cancelled'),
    )
    a_number = models.CharField(max_length=20, primary_key="true")
    account_name = models.CharField(max_length=50, null=True, blank=True, default="")
    account_status = models.CharField(max_length=40, choices=STATUS, null=True, blank=True, default="")
    address = models.CharField(max_length=300, null=True, blank=True, default="")
    country = models.CharField(max_length=50, null=True, blank=True, default="")
    exit_rate = models.IntegerField(null=True, blank=True, default=0)
    exit_rate_usd = models.IntegerField(null=True, blank=True, default=0)
    oppertunity_type = models.IntegerField(null=True, blank=True, default=0)
    ultimate_parent = models.CharField(max_length=50, null=True, blank=True, default=None)
    sfdc_segmentation = models.CharField(max_length=300, null=True, blank=True, default="")
    org_type_1 = models.CharField(max_length=50, null=True, blank=True, default=None)
    org_type_2 = models.CharField(max_length=50, null=True, blank=True, default=None)
    org_type_3 = models.CharField(max_length=50, null=True, blank=True, default=None)
    org_type_4 = models.CharField(max_length=300, null=True, blank=True, default=None)
    org_type_5 = models.CharField(max_length=300, null=True, blank=True, default=None)
    last_updated = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    segment_source = models.CharField(max_length=300, null=True, blank=True, default=None)
    entity_url = models.CharField(max_length=300, null=True, blank=True, default=None)
    unavailable = models.CharField(max_length=300, null=True, blank=True, default="")
    modified = models.DateTimeField(verbose_name='date_modified', auto_now=True)

    def __str__(self):
        return self.a_number
