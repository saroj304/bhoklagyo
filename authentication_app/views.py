from django.conf import settings
import http.client
import random
from django.core.mail import send_mail
from django.conf import settings

def send_otp_via_email(email):
    subject = "Your account verification email"
    otp = str(random.randint(100000,999999))
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message , email_from , [email])














def sendOtp(phone):
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.authkey
    headers ={'content-type':"application/json"}
    otp = str(random.randint(1000,9999))
    url = "http://control.msg91.com/api/sendotp.php?otp="+otp+'sender=ABC&message='+'Your otp is '+ otp +'&mobile='+phone+'&authkey='+authkey+'&country=91'
    conn.request('GET',url,headers=headers)
    res = conn.getresponse()
    data = res.read()
    return None