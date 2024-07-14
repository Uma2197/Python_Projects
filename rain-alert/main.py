import requests
import smtplib
# Angela uses twilio to send SMS. we cant install the package here, donno why
# So I sent email.
MY_LAT = 51.760689
MY_LONG = 14.327580
api_key = "8ad9f42f30824a3687cdd3beeb9f2058"
my_email = "uma.dv1819@gmail.com"
password = "dfqo rxgg cdcq ozgo"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 7,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="maggi2197@gmail.com", msg="Its cloudy!!")
