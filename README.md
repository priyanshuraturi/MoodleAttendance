# Moodle Attendance

Python Selenium Project to Mark Attendance on Moodle Platform Regularly

## Installation

Clone The Repository , install the requirements , enter your credentials in user.json.

```bash
pip install -r requirements.txt
```
## Run
```bash
python main.py
```
## Task Scheduling
Task Like Marking Attendance and Sending Application Status Can Be Scheduled To Your Desired Time
This Functionality is Added Because this app was made to run on VPS 24 x 7 hence Scheduling Plays a Important Role.

```python
scheduler1 = schedule.Scheduler()
scheduler1.every().day.at("06:00").do(markAttendance)
#You Can Add Your Desired Time in 24 Hour Format To Schedule Your Task 
scheduler3 = schedule.Scheduler()
scheduler3.every().day.at("05:00").do(sendAdmin, "App Running Perfectly Fine")
```
If You Don't want functionality like scheduling you can use only mark.py file , by just uncommenting the last line 

```python
#markAttendace()
```

## User.json File

```json
[
  {
    "id": "MoodleId",
    "pass": "Moodle Password",
     "email": "exapmple@gmail.com",
    "name": "User's Name"
  }
]

```
You Can add as many Users in This Json File
## Enviroment Variables

```env
senderMail= SenderMail Here
senderPassword = Sender Password Here
adminMail = Admin Mail
```
The Files User.json and credentials.env File is important ,Please add these files according to above templates.


## License
[MIT](https://choosealicense.com/licenses/mit/)
