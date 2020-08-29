# Script Title: Bulk-Email-Sender
# Bulk Email Sender Script with Attachment
# Date: 29-09-2020
# Help Menu- python3 bulk-email-sender.py -h
# Script Usage- python3 bulk-email-sender.py --list /root/Desktop/email.txt --name "Your Name" --email senderemail@example.com --password sender_password --subject "Email Subject Here" --body /root/Desktop/body.txt

#!/usr/bin/python3

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.message import Message
from email import encoders
from pathlib import Path
import mimetypes
import argparse
import smtplib
import sys


print('')
print("==================================================================================================================================")
print('#																#')
print("# =====================================	Welcome To Python Bulk Mail Sender Script  ============================================ #")
print('#																#')
print("==================================================================================================================================")
print('Made By- Aves Ahmed Khan')
print('')
print('If You Have Any Query PM me at:')
print('Twitter  - https://twitter.com/av3sk77')
print('LinkedIn - https://www.linkedin.com/in/aves-ahmed-khan-b835a7168/')
print('')

parser = argparse.ArgumentParser()

parser.add_argument("--attach", help='Add Attachment [Ex. --attach "/root/Desktop/mail.csv"]')

requiredNamed = parser.add_argument_group('Required Arguments')
requiredNamed.add_argument("--list", help='Emails List Location [Ex. --list "/root/Desktop/mails.txt"]', type=Path, required=True)
requiredNamed.add_argument("--name", help='Email Sender_Name [Ex. --name "firstname lastname"]', type=str, required=True)
requiredNamed.add_argument("--email", help='Sender Email Address [Ex. --email sender@example.com]', type=str, required=True)
requiredNamed.add_argument("--password", help='Sender Email Password [Ex. --password Password@123]', type=str, required=True)
requiredNamed.add_argument("--subject", help='Subject Content [Ex. --subject "Enter Subject Here"]', type=str, required=True)
requiredNamed.add_argument("--body", help='Body Content Location [Ex. --body "/root/Desktop/BodyContent.txt"]', type=Path, required=True)

args = parser.parse_args()

email_list = args.list
sender_name = args.name
sender_email = args.email
sender_password = args.password
email_subject = args.subject
email_body = args.body
email_attach = args.attach
attached = ''

if not email_list.exists() & email_list.is_file():
    print("Email list File Not Found:", email_list)
    sys.exit()
if not email_body.exists() & email_body.is_file():
   print("Body Content File Not Found:", email_body)
   sys.exit()

if email_attach is not None:
    if not Path(email_attach).exists() & Path(email_attach).is_file():
        print("Attchment File", email_attach, "Not Found")
        sys.exit()
    else:
        attached = Path(email_attach)

with open(email_body, 'r') as file:
    message_body = file.read()
try:
    with open(email_list, "r") as email_list_file:
        for list in email_list_file:
            if attached == '':

                message = MIMEMultipart()
                message["from"] = sender_name
                message["to"] = list
                message["subject"] = email_subject
                message.attach(MIMEText(message_body))

                with smtplib.SMTP(host="smtp.gmail.com", port=587) as mail:
                    mail.ehlo()
                    mail.starttls()
                    mail.login(sender_email, sender_password)
                    mail.send_message(message)
                    print("Successfully Sent to", list, end='')
            else:

                message = MIMEMultipart()
                message["from"] = sender_name
                message["to"] = list
                message["subject"] = email_subject
                message["body"] = message_body
                message.attach(MIMEText(message_body))

                filename = email_attach
                file_name = attached.name
                attachment = open(filename, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + file_name)
                message.attach(part)
                text = message.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, list, text)
                server.quit()
                print("Successfully Sent to", list, end='')

except smtplib.SMTPAuthenticationError:
    print("Make Sure You have Entered Valid Credentials")
    print('')
    print("And you have Enabled the Less Secure App")
    print("If haven't done Please Follow this Link- https://github.com/av3sk77/Bulk-Email-Sender/blob/master/README.md")
except smtplib.SMTPRecipientsRefused:
    print(f"Make Sure You have Provide Email List file is Correct")
else:
    print('')
    print("Thank You For Using This Script")