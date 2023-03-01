from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


#variables
email_sender = ""
email_password = password

email_receiver = "mixet97888@letpays.com"

subject = "Test subject"
body = """
Testing the body paragraph of an email.
"""



#creating EmailMessage instance
em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


#sending the email
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


