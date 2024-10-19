from twilio.rest import Client

from configs.twilioconf import account_sid,auth_token,from_number
client = Client(account_sid, auth_token)


def send_sms(phone_number, textctn):
    print(phone_number,textctn)
    try:
        message = client.messages.create(
            to=f"+{phone_number}",
            from_=from_number,
            body=f"{textctn}"
        )
        return "✅ Message Send As Successfully."
    except Exception as e:
        print(e)
        return "❌ Message As Failed To Send."
        
