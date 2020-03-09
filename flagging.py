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

def read_audit():
	url = 'https://graph.microsoft.com/v1.0/auditLogs/signIns'
	auth_token=get_token()
	headers = {'Authorization': 'Bearer ' + auth_token}

	response = requests.get(url, headers=headers)
	
	output_dict = [x for x in response.json()['value'] if x['userId'] == 'a954142e-8758-44f1-89c2-67efbfc31b82' and x['status']["errorCode"]>0 ]
	with open('data.json', 'w') as f:
		json.dump(output_dict, f)


read_audit()