import requests
import os
from twilio.rest import Client
API_KEY = "3b3113ab7cd10eed0e52ac1aacc807bd"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
PARAMs = {
    # "q": "Noida",
    "lat": 77.33,
    "lon": 28.58,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
# response = requests.get(url="http://api.openweathermap.org/data/2.5/weather", params=PARAMs)
response = requests.get(url=OWM_Endpoint, params=PARAMs)
response.raise_for_status()
# print(response.json()["hourly"])
hourly_weather_list = response.json()["hourly"][:12]
account_sid = "AC3aa948807f095c178288479469e1089c"
auth_token = "c7a0e6cefe2ff4d1cbdc929820a78b70"
print(type(hourly_weather_list))

will_rain = False
for data in hourly_weather_list:
    if (data["weather"][0]['id']) < 700:
        # print("Bring Umbrella")
        # will_rain = True
        print("DO nothing")

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Might rain today ☔",
        from_='+18596462729',
        to='+919958098549'
    )

    print(message.status)