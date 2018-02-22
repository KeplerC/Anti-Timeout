#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.header import Header


from twilio.rest import Client
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config

def send_sms(content, phone):
    if(content == ""):
        return False
    
    client = Client(config.account, config.token)
    message = client.messages.create(to=phone, from_ = config.phone, body=content)
    return True


mail_host="smtp.mailgun.org"
mail_user="postmaster@sandbox771d908665d24655b9cd402f4ece3dc8.mailgun.org"   
mail_pass="bfce1771c370570883fd229be0f3638a"

TERM = '18S'

def sendEmail(content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("UCLA Class Assistant", 'utf-8')
    message['To'] =  Header("Kepler", 'utf-8')
    message['Subject'] = Header("Class Update", 'utf-8')
    #try:
    receivers = ["chenkaiyuan@ucla.edu"]
    sender = "chenkaiyuan@ucla.edu"
    smtpObj = smtplib.SMTP('smtp.mailgun.org', 587)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print "success"

        
if __name__ == "__main__":
    sendEmail("main.py is DEAD")