import twilio
from twilio.rest import Client
import random
from django.views import View  

#Functions here of SMS 
def gen_otp():
    OTP = random.randint(1000,9999)
    return OTP


account_sid = 'AC61b7224f42a7acd7b97e5b7000df43dd'
auth_token = 'eba1bf0a4e93fdb23d57dd6cbf6e7f4d'
client = Client(account_sid, auth_token)

def send_sms(phone_number, OTP):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                     body="Your OTP is" +str(OTP),
                     from_='+18304338615',
                     to= phone_number
                 )
    return message.sid