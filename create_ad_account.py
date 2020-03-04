import requests


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

	print(x.text)

def create_ads_create():
	url = 'https://www.w3schools.com/python/demopage.php'
	myobj = {'somekey': 'somevalue'}

	x = requests.post(url, data = myobj)

	print(x.text)

	auth_token='kbkcmbkcmbkcbc9ic9vixc9vixc9v'
	hed = {'Authorization': 'Bearer ' + auth_token}
	data = {'app' : 'aaaaa'}

	url = 'https://api.xy.com'
	response = requests.post(url, json=data, headers=hed)
	print(response)
	print(response.json())


get_token()