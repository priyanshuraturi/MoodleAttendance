import smtplib
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
import os

from dotenv.main import dotenv_values

dotenv_path = Path('./credentials.env')
load_dotenv(dotenv_path=dotenv_path)


def sendMail(messages):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    senderEmail = os.getenv('senderMail')
    senderPassword = os.getenv('senderPassword')
    s.login(senderEmail, senderPassword)
    for msg in messages:
        s.send_message(msg)
    s.quit()


def sendAdmin():
    msg = EmailMessage()
    msg.set_content("App is Running Perfectly Fine\n Time:" +
                    str(datetime.now()))
    msg['Subject'] = "App Running"
    msg['From'] = "Priyanshu Raturi"
    msg['To'] = os.getenv('adminMail')
    messages = []
    messages.append(msg)
    sendMail(messages)


def sendErrRep(error):
    msg = EmailMessage()
    error = str(error)
    msg.set_content("Ops There's and Error\n Time:" + error +
                    str(datetime.now()))
    msg['Subject'] = "App Running"
    msg['From'] = "Priyanshu Raturi"
    msg['To'] = os.getenv('adminMail')
    messages = []
    messages.append(msg)
    sendMail(messages)


sendAdmin()
