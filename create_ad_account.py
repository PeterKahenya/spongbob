import requests
import json


def get_token():
	url="https://login.microsoftonline.com/4370dcec-f44f-47ec-a5a6-2cd0ec017a72/oauth2/token"
	data={
		"grant_type":"client_credentials",
		"client_id":"bba23e01-d3e5-4ba3-b7bc-51ffada2ccf9",
		"client_secret":"v]h?-ih0f67A6h?Tp:x]H9qx.kLNH:XW",
		"resource":"https://graph.microsoft.com"
	}
	headers = {"Content-Type": "application/x-www-form-urlencoded"}
	x=requests.post(url,data=data,headers=headers)

	return json.loads(x.text)["access_token"]

def create_ad_account():
	url = 'https://graph.microsoft.com/v1.0/users'
	auth_token=get_token()
	headers = {'Authorization': 'Bearer ' + auth_token}

	
	user_obj = {
				  "accountEnabled": True,
				  "displayName": "Peter Kahenya",
				  "mailNickname": "kahenya",
				  "userPrincipalName": "kahenya@terowamzgmail.onmicrosoft.com",
				  "passwordProfile" : {
				    "forceChangePasswordNextSignIn": True,
				    "password": "ADAS#2020"
				  }
				}

	response = requests.post(url, json=user_obj, headers=headers)

	print(response.json())

def disable_ad_account():
	url = 'https://graph.microsoft.com/v1.0/users/90a48acd-fbcd-4ba9-bb2b-a9d1203fc8a4'
	auth_token=get_token()
	headers = {'Authorization': 'Bearer ' + auth_token}

	
	updated_user = {
				  "accountEnabled": False
				}

	response = requests.patch(url, json=updated_user, headers=headers)

	print(response.status_code)



disable_ad_account()