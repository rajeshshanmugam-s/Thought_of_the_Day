import smtplib, ssl
import json
import random

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open('data/quotes_1.json') as file:
    data = json.load(file)

def quote_finder():
    while True:
        rand_no = random.randint(0,1643)
        if not data[rand_no]['Shared']:
            data[rand_no]['Shared'] = True
            with open('data/quotes_1.json', 'w+') as file:
                json.dump(data, file)
            return data[rand_no]

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sender@mail.com"
receiver_email = "receiver@mail.com"
password = "password"
message = """\
Subject: Hi there
"""+quote['text']+"""\

# message = """\
# Subject: Hi there
# """+quote['text']+"""\
#
#
# ~"""+quote['author']

message = MIMEMultipart()
message['From'] = sender_email
# message['To'] = receiver_email
message['Subject'] = "[Testing]Thought of the Day"
message['To'] = 'rallyrajesh@gmail.com'

text = quote['text'] + """  
~"""+quote['author']

text = MIMEText(text, "plain")

message.attach(text)

message = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
