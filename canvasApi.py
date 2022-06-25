from twilio.rest import Client
from canvasapi import Canvas
from datetime import datetime

account_sid = "***" # account sid from Twilio

auth_token = "***" # authorization token from Twilio

client = Client(account_sid, auth_token)


API_KEY = "***" # API Key from Canvas
API_URL = "***" # URL for Canvas

canvas = Canvas(API_URL, API_KEY)

course = canvas.get_course(******) # enter course number where * is which can be found on Canvas
# list all additional courses similarly
assignmentsList = course.get_assignments(bucket = 'upcoming')
# list all additional assignments from assignments

work = []
formated_list = []

for i in assignmentsList:
    formated = datetime.strptime(i.due_at, "%Y-%m-%dT%H:%M:%SZ")
    formated_list.append(formated)

work.append(formated_list)

# repeat above for all assignments

iterator = 0

for i in range(len(work)):
    for j in range(len(work[i])):
        if (work[i][j].date() == datetime.now().date()):
            iterator += 1


message = client.api.account.messages.create(
        to = "+**********", # personal phone number
        from_ = "+**********", # phone number from Twilio
        body = f"There are {iterator} assignments due today!"
)
