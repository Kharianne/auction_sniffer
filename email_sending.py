from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json


class Email:
    def __init__(self, server):
        self.msg = MIMEMultipart()
        with open('credentials.json') as credentials_file:
            self.data = json.load(credentials_file)
        self.password = self.data['password']
        self.msg['From'] = self.data['from']
        self.server = smtplib.SMTP(server)

    def send_email(self, recipient, subject, message):
        self.msg.attach(MIMEText(message, 'plain'))
        self.msg['To'] = recipient
        self.msg['Subject'] = subject
        self.server.starttls()
        self.server.login(self.msg['From'], self.password)
        self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        self.server.quit()





