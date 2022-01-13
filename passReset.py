import smtplib
import json
from pathlib import Path
from dotenv import load_dotenv
import os
from email.message import EmailMessage


dotenv_path = Path('./credentials.env')
load_dotenv(dotenv_path=dotenv_path)

file = open('./users.json',)
users = json.load(file)
userCount = len(users)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
senderEmail = os.getenv('senderMail')
senderPassword = os.getenv('senderPassword')
s.login(senderEmail, senderPassword)
while userCount != 0:
    msg = EmailMessage()
    msg.set_content(f'Hi {users[userCount - 1]["name"]},\n as per new online semester is started, Moodle Passwords are retested to Default.\n'
                    f'Please Change your Password to Previous Moodle Password.\n For You which is [{users[userCount - 1]["pass"]}] \nElse I Wouldn\'t '
                    f'be able to mark your attendance\n'
                    f'Regards\n'
                    f'Priyanshu')
    msg['Subject'] = "Password Reset"
    msg['From'] = "Moodle Attendance IMPORTANT"
    msg['To'] = users[userCount - 1]["email"]
    s.send_message(msg)
    print(f'Mail Sent To {users[userCount - 1]["email"]}')
    userCount = userCount-1





