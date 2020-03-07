from django.db import models
import uuid
import requests
import json


class CreditCardAsset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_of_asset = models.CharField(max_length=50)
    name_of_asset = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    credit_card_number = models.CharField(max_length=100)
    credit_card_exp_date = models.CharField(max_length=20)
    credit_card_cvc = models.CharField(max_length=200)
    credit_card_issuer = models.CharField(max_length=256)

    def disable(self):

        pass


class ActiveDirectoryAsset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_of_asset = models.CharField(max_length=50)
    name_of_asset = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    username = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    groups = models.CharField(max_length=50, blank=True)
    roles = models.CharField(max_length=50, blank=True)
    block_sign_in = models.CharField(max_length=50, blank=True)
    usage_location = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=50, blank=True)
    ad_account_id = models.CharField(max_length=100, blank=True)

    def get_token(self):
        url = "https://login.microsoftonline.com/4370dcec-f44f-47ec-a5a6-2cd0ec017a72/oauth2/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": "bba23e01-d3e5-4ba3-b7bc-51ffada2ccf9",
            "client_secret": "v]h?-ih0f67A6h?Tp:x]H9qx.kLNH:XW",
            "resource": "https://graph.microsoft.com"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        x = requests.post(url, data=data, headers=headers)
        return json.loads(x.text)["access_token"]

    def disable(self):
        print(self.ad_account_id)
        print("Disable on child")

        url = 'https://graph.microsoft.com/v1.0/users/' + self.ad_account_id
        auth_token = self.get_token()
        headers = {'Authorization': 'Bearer ' + auth_token}
        updated_user = {"accountEnabled": False}
        response = requests.patch(url, json=updated_user, headers=headers)

        return response.status_code


    def __str__(self):
        return self.name_of_asset
