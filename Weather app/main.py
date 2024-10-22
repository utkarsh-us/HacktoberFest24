import requests
import os
from twilio.rest import Client

OWM = "" #OPEN WEATHERMAP API
api_key = ""#APIKEY

acc_ssid = "" #Twilio Account SID
auth_tkn = "" #Twilio Auth Token
app = Client(acc_ssid, auth_tkn)

parameters = {
    "lat": 37.916248,#Lattitude
    "lon": 40.225590,#Longitude
    "appid": api_key,
    "cnt": 4 #Number of days
}

response = requests.get(OWM, params=parameters)
var = response.status_code
response.raise_for_status()
print(f"status code: {var}")
weather_data = response.json()
print(weather_data)

weather_list = weather_data['list']
weather_id = weather_list[0]['weather'][0]['id']
just = 0
id_list = []
for i in range(4):
    weather_idd = weather_list[i]['weather'][0]['id']
    id_list.append(weather_idd)

print(id_list)
rain = False
for ids in id_list:
    if ids < 700:
        rain = True

message = app.messages.create(
        body="love ur self",
        from_="+12177675760",
        to="+918714094884"
    )

if rain:
    print(message.sid)
