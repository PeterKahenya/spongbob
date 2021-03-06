from django.db import models
import uuid
import requests
import json


class Asset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_of_asset = models.CharField(max_length=50)
    name_of_asset = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name_of_asset


class CreditCardAsset(Asset):
    credit_card_number = models.CharField(max_length=100)
    credit_card_exp_date = models.CharField(max_length=20)
    credit_card_cvc = models.CharField(max_length=200)
    credit_card_issuer = models.CharField(max_length=256)

    def disable(self):
        pass


class ActiveDirectoryAsset(Asset):
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
        url = 'https://graph.microsoft.com/v1.0/users/'+self.ad_account_id
        auth_token = self.get_token()
        headers = {'Authorization': 'Bearer ' + auth_token}
        updated_user = {"accountEnabled": False}
        response = requests.patch(url, json=updated_user, headers=headers)

        return response.status_code

    def enable(self):
        url = 'https://graph.microsoft.com/v1.0/users/'+self.ad_account_id
        auth_token = self.get_token()
        headers = {'Authorization': 'Bearer ' + auth_token}
        updated_user = {"accountEnabled": True}
        response = requests.patch(url, json=updated_user, headers=headers)

        return response.status_code

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

    def read_audit(self):
        url = 'https://graph.microsoft.com/v1.0/auditLogs/signIns'
        auth_token = self.get_token()
        headers = {'Authorization': 'Bearer ' + auth_token}
        response = requests.get(url, headers=headers)

        output_dict = [x for x in response.json()['value']
                       if x['userId'] == self.ad_account_id]
        return output_dict

    def get_flags(self):
        url = 'https://graph.microsoft.com/v1.0/auditLogs/directoryAudits'
        auth_token = self.get_token()
        headers = {'Authorization': 'Bearer ' + auth_token}
        response = requests.get(url, headers=headers)
        list_of_events = response.json()['value']

        suspicious_events = []
        for event in list_of_events:
            affectedResource = event['targetResources'][0]

            if affectedResource['id'] == self.ad_account_id:
                targetUserAffectedResource = affectedResource
                if targetUserAffectedResource["modifiedProperties"]:
                    if targetUserAffectedResource["modifiedProperties"][0]["newValue"] == "[true]" and targetUserAffectedResource["modifiedProperties"][0]["oldValue"] == "[false]":
                        suspicious_events.append(event)

        return suspicious_events
