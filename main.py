import requests
from twilio.rest import Client

OWM_Endpoint = "api_link"
api_key  = "api_key"
user_sid = "your_sid"
auth_token = "auth_token"

weather_params = {
    "lat": 40.185780, #latitude and longitude of your location address where you live
    "lon": 29.056660,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:  
    client = Client(user_sid,auth_token)
    message = client.messages.create(
  from_='whatsapp:+12345678911',
  #content_sid='HXb5b6564564564129ad7c8efe1f983e',
  body="I MADE ITTTTT YEEEYYYY!!!!!!!",
  to='whatsapp:+12345678911'
)

print(message.sid)
    