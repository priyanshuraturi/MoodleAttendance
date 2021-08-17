from email.message import EmailMessage
from selenium import webdriver
import time
from datetime import datetime
import json
from mailer import sendMail, sendErrRep


def markAttendance():
    try:
        mailList = []
        flag = 0
        logMsg = "Hi \n"
        subjectList = []
        file = open('./users.json',)
        users = json.load(file)
        userCount = len(users)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(("--no-sandbox"))
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            './chromedriver', chrome_options=chrome_options)
        driver.get('http://45.116.207.67/moodle/login/index.php')
        while(userCount != 0):
            print(users[userCount - 1]['name'])
            driver.find_element_by_id('username').send_keys(
                users[userCount - 1]['id'])
            driver.find_element_by_id('password').send_keys(
                users[userCount - 1]['pass'])
            driver.find_element_by_id('loginbtn').click()
            time.sleep(1)
            continueLink = driver.find_elements_by_link_text("Today")
            if not continueLink:
                print("No Attendace For Today:")
                msg = EmailMessage()
                msg.set_content("No Attendance For Today")
                msg['Subject'] = 'Moodle Attendance'
                msg['From'] = "Priyanshu Raturi"
                msg['To'] = "Priyanshuraturi@gmail.com"
                mailList.append(msg)
                break

            continueLink[0].click()
            activityList = driver.find_elements_by_link_text('Go to activity')
            numberOfElems = len(activityList)
            print(numberOfElems)
            while(numberOfElems > 0):
                time.sleep(1)
                activityList = driver.find_elements_by_link_text(
                    'Go to activity')
                try:
                    if activityList[numberOfElems - 1].is_enabled:
                        activityList[numberOfElems - 1].click()
                    else:
                        numberOfElems -= 1
                        continue
                except:
                    numberOfElems -= 1
                    continue
                time.sleep(1)
                submitLink = driver.find_elements_by_link_text(
                    'Submit attendance')
                if(len(submitLink) > 0):
                    submitLink[0].click()
                    heading = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[3]/header/div/div/div/div[1]/div[1]/div/div/h1").text
                    subjectList.append(heading)
                    print(heading)
                    driver.find_element_by_xpath(
                        '/html/body/div[2]/div[3]/div/div/section/div[1]/form/fieldset/div/div/div[2]/fieldset/div/label[1]/input').click()
                    time.sleep(3)
                    driver.find_element_by_id('id_submitbutton').click()
                    driver.back()
                    driver.back()
                driver.back()
                numberOfElems -= 1
            if not subjectList:
                print("No Mail Send to ",
                      users[userCount-1]['name'], " ,All Subjects Are Marked")
                logMsg += users[userCount - 1]['name'] + " \n"
                flag = 1
            else:
                message = "Hi,\n " + \
                    users[userCount - 1]['name'] + \
                    ",\n Your Subjects Attendace For: \n"
                for ele in subjectList:
                    message += ele+"\n"
                message += "was marked Succesfully ;-)"
                msg = EmailMessage()
                msg.set_content(message)
                msg['Subject'] = 'Moodle Attendance'
                msg['From'] = "Priyanshu Raturi"
                msg['To'] = users[userCount - 1]['email']
                mailList.append(msg)
                print(msg)
            driver.delete_all_cookies()
            driver.get('http://45.116.207.67/moodle/login/index.php')
            userCount -= 1
        if(flag == 1):
            msg = EmailMessage()
            msg.set_content(
                logMsg+"Had No Attendance\n Time:"+str(datetime.now()))
            msg['Subject'] = "App Running"
            msg['From'] = "Priyanshu Raturi"
            msg['To'] = "Priyanshuraturi@gmail.com"
            flag = 0
            mailList.append(msg)

        sendMail(mailList)
    except Exception as e:
        print(e)
        userCount -= 1
        sendErrRep(e)


#markAttendance()
