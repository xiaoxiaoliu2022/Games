
API_KEY = "fe1648265520c43bafcc258733b4704d"
LAT = 47.608013
LON = -122.335167
EXCLUSION = "daily,minutely,currently"
import requests
from twilio.rest import Client
account_sid = 'AC93f5b5f5e50bd665b3d44b05a1b2040d'
auth_token = 'cb4a01409b075dbe6a14155867ccd1d2'
parameter = {
    "lat": LAT,
    "lon": LON,
    "exclude": EXCLUSION,
    "appid": API_KEY
}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
data = response.json()
print(data)
hourly_weather = data["hourly"]
# weather_slice = hourly_weather[:12]
for hourly_data in weather_slice
for hour in range(0, 13):
    weather_code = hourly_weather[hour]["weather"][0]["id"]
    if weather_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="🌷Bring your umbrella and have a bright day. You are the best, be confident!🍀",
        from_='+17409088349',
        to='+12066370459'
    )
    print(message.status)