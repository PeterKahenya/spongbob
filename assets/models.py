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

class CreditCardAsset(Asset):
    credit_card_number=models.CharField(max_length=100)
    credit_card_exp_date=models.CharField(max_length=20)
    credit_card_cvc=models.CharField(max_length=200)
    credit_card_issuer=models.CharField(max_length=256)

    def disable(self):
        pass