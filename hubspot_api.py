from hubspot import HubSpot
import requests
from fake_useragent import UserAgent
from hubspot.crm.contacts import ApiException
token = 'pat-na1-89d96e4f-c32d-4c6f-ad49-fe77040a94b1'
api_client = HubSpot(access_token=token)
import hubspot
import json

def create_contact():
    user_agent = UserAgent()
    headers = {
        'User-Agent': user_agent.random,
        'Content-Type': 'application/json',
    }
    data = {
        "duration": 900000,
        "email": "jaftontest1@gmail.com",
        "firstName": "Jafton2",
        "formFields": [],
        "guestEmails": [],
        "lastName": "Test2",
        "locale": "ru-ru",
        "offline": False,
        "startTime": 1700838900000,
        "timezone": "Asia/Tashkent"
    }

    url = 'https://api.hubspot.com/meetings-public/v1/book?slug=quvonchbek'
    response = requests.post(url=url, headers=headers, json=data)

    print(response.json())



def get_contacts():
    all_contacts = api_client.crm.contacts.get_all()
    for i in all_contacts:
        print('---------------------')
        try:
            contact_fetched = api_client.crm.contacts.basic_api.get_by_id(i.id)
            print(contact_fetched)
        except ApiException as e:
            print("Exception when requesting contact by id: %s\n" % e)

client = hubspot.Client.create(access_token=token)
api_response = client.crm.contacts.basic_api.get_page(limit=10, archived=False)
# with open('data.json', 'w') as f:
#     json.dump(api_response, f, indent=4)
# for i in api_response.results:
#     print('------------------------------')
#     print(i)
print(api_response)