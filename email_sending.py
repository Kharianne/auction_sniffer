from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Email:
    def __init__(self, server, password, _from):
        self.msg = MIMEMultipart()
        self.password = password
        self.msg['From'] = _from
        self.server = smtplib.SMTP(server)

    def send_email(self, recipient, subject, message):
        self.msg.attach(MIMEText(message, 'plain'))
        self.msg['To'] = recipient
        self.msg['Subject'] = subject
        self.server.starttls()
        self.server.login(self.msg['From'], self.password)
        self.server.sendmail(self.msg['From'], self.msg['To'], self.msg.as_string())
        self.server.quit()





