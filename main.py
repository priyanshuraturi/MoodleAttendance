import schedule
import time
from mark import markAttendance
from datetime import datetime
from mailer import sendAdmin
from email.message import EmailMessage


scheduler1 = schedule.Scheduler()
scheduler1.every().day.at("06:00").do(markAttendance)
scheduler2 = schedule.Scheduler()
scheduler2.every().day.at("08:30").do(markAttendance)
scheduler3 = schedule.Scheduler()
scheduler3.every().day.at("05:00").do(sendAdmin)
scheduler4 = schedule.Scheduler()
scheduler4.every().day.at("14:15").do(sendAdmin)
falg = 0
print("Started")
print(datetime.now())
count = 0
while True:
    scheduler1.run_pending()
    scheduler2.run_pending()
    scheduler3.run_pending()
    scheduler4.run_pending()
    time.sleep(1)
    count += 2
    if(count == 7200):
        count = 0
        print(datetime.now())
