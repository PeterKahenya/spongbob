from django.db import models
import uuid
import requests


class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_of_asset = models.CharField(max_length=50)
    name_of_asset = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    # id_of_asset = models.TextField()
    # More fields

    def __str__(self):
        return self.name_of_asset
    
class CreditCardAsset(Asset):
    credit_card_number=models.CharField(max_length=100)
    credit_card_exp_date=models.CharField(max_length=20)
    credit_card_cvc=models.CharField(max_length=200)
    credit_card_issuer=models.CharField(max_length=256)

    def disable(self):
        pass


class ActiveDirectoryAsset(Asset):
    username=models.CharField(max_length=500,blank=True)
    name=models.CharField(max_length=50,blank=True)
    first_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    groups=models.CharField(max_length=50,blank=True)
    roles=models.CharField(max_length=50,blank=True)
    block_sign_in=models.CharField(max_length=50,blank=True)
    usage_location=models.CharField(max_length=50,blank=True)
    job_title=models.CharField(max_length=50,blank=True)
    department=models.CharField(max_length=50,blank=True)

    #this is an active directory user account



    def create(self):
        pass
    def disable(self):
        pass
