import requests
import json
import threading
from django.core.mail import EmailMessage


def get_token():
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


def get_flags():
    url = 'https://graph.microsoft.com/v1.0/auditLogs/directoryAudits'
    print("fetching flags")

    auth_token = get_token()

    headers = {'Authorization': 'Bearer ' + auth_token}
    response = requests.get(url, headers=headers)
    list_of_events = response.json()['value']

    suspicious_events = []
    for event in list_of_events:
        affectedResource = event['targetResources'][0]
        suspicious_events.append(event)
    if len(suspicious_events):
        email = EmailMessage(
            'Logs Here',
            'Body goes here'+str(suspicious_events),
            'terrymwangi05@gmail.com',
            ['terrymwangi05@gmail.com'],
            [],
            reply_to=['terrymwangi05@gmail.com'],
        )
        email.send()

    # threading.Timer(5.0, get_flags).start()


def start_flags_listener():
    print("Started flags listener")
    # threading.Timer(5.0, get_flags).start()
