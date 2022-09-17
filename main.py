import requests
import smtplib
import ssl


my_email = "your-mail"
password = "your-password"
api_key = "7c08e67ecf404390dd00cb771f5bac83"
account_sid = "AC72866446a8bdad3a0084d479c0de5e73"
auth_token = "b61d52e949539f7459b6ad779136ddd1"
parameters = {
    "lat": 6.465422,
    "lon": 3.406448,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]
new_data = data[:11]
wil_rain = False
for weather in new_data:
    condition = weather["weather"][0]["id"]
    if condition < 600:
        wil_rain = True
if wil_rain:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="coolpellajosh@gmail.com",
                            msg=f"Subject: Weather Report\n\nIt's going to rain today!")