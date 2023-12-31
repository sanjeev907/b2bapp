import twilio
from twilio.rest import Client
import random
from django.views import View  
from rest_framework.pagination import PageNumberPagination

#Functions here of SMS 
def gen_otp():
    OTP = random.randint(1000,9999)
    return OTP


account_sid = 'AC61b7224f42a7acd7b97e5b7000df43dd'
auth_token = '1ed36278eb81c75071e4bbb6be4e691e'
client = Client(account_sid, auth_token)

def send_sms(phone_number, OTP):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                     body="Your OTP is" +str(OTP),
                     from_='+18304338615',
                     to= phone_number
                 )
    return message.sid


# Custom Paginations Starts From Here

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100