# Bulk-Email-Sender
Bulk-Email-Sender Python Script will send bulk email from one Script. You can Also Add the Attachment with this Script. This script work on both Windows and Linux Operating System. This script only works on Python3 version So, you must be Install Python3 Version.

## Requirement
You must be Install Python3 Version-<br/>
You can Download the Python3 from this link-
https://www.python.org/downloads/

### Allow less secure app
Before Run this Script Make Sure you have enable the Less Secure App Accees.<br/>
Link- https://myaccount.google.com/u/1/lesssecureapps
![alt text](https://github.com/av3sk77/Bulk-Email-Sender/blob/master/less-secure-app.png?raw=true)
## Before Run the Script
Create Two text files which contain the email lists and the Body part Like-

### email_list.txt
```bash
first@example.com
sencond@example.com
third@example.com
```

### body.txt
```bash
Hello Sir/Madam,

This is Python Script.
Which is Send Bulk Email from one Script.

Made By-
Aves Ahmed Khan

Thanks For Using this Script
```

## How To Work
### Help Menu
```bash
# python3 bulk-email-sender.py -h

usage: bulk-email-sender.py [-h] [--attach ATTACH] --list LIST --name NAME --email EMAIL --password PASSWORD --subject SUBJECT --body BODY

optional arguments:
  -h, --help           show this help message and exit
  --attach ATTACH      Add Attachment [Ex. --attach "/root/Desktop/mail.csv"]

Required Arguments:
  --list LIST          Emails List Location [Ex. --list "/root/Desktop/mails.txt"]
  --name NAME          Email Sender_Name [Ex. --name "firstname lastname"]
  --email EMAIL        Sender Email Address [Ex. --email sender@example.com]
  --password PASSWORD  Sender Email Password [Ex. --password sender_password]
  --subject SUBJECT    Subject Content [Ex. --subject "Enter Subject Here"]
  --body BODY          Body Content Location [Ex. --body "/root/Desktop/body.txt"]
```
  
### Usage
#### Send Email Without Attachment
```bash
# python3 bulk-email-sender.py --list /root/Desktop/email.txt --name "Your Name" --email senderemail@example.com --password sender_password --subject "Email Subject Here" --body /root/Desktop/body.txt
```

#### Send Email With Attachment
```bash
# python3 bulk-email-sender.py --list /root/Desktop/email.txt --name "Your Name" --email senderemail@example.com --password sender_password --subject "Email Subject Here" --body /root/Desktop/body.txt --attach /root/Desktop/mail.csv
```
  

