# Moodle Attendance

Python Selenium Project to Mark Attendance on Moodle Platform Regularly

## Installation

Clone The Repository , install the requirements , enter your credentials in user.json.

```bash
pip install requirements.txt
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
