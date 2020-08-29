# Bulk-Email-Sender
Bulk-Email-Sender Python Script will send bulk email from one Script. This script work on both Windows and Linux Operating System. This script only work on Python3 version So, you must be Install Python3 Version.

## Requirement
You must be Install Python3 Version-<br/>
You can Download the Python3 from this link-
https://www.python.org/downloads/

## Before Run the Script
Make text files which contain the email list and the Body Contains Like-

<b>email_list.txt</b><br/>
first@example.com<br/>
sencond@example.com<br/>
third@example.com<br/>

<b>body.txt</b><br/>
Hello Sir/Madam,<br/>
This is Python Script.<br/>
Which is Send Bulk Email from one Script.<br/>
Made By-<br/>
Aves Ahmed Khan<br/>
<br/>
Thanks For Using this Script<br/>

## How To Work
### Help Menu
<b># python3 bulk-email-sender.py -h</b><br/>
usage: bulk-email-sender.py [-h] [--attach ATTACH] --list LIST --name NAME --email EMAIL --password PASSWORD --subject SUBJECT --body BODY<br/>
<br/>
optional arguments:<br/>
  -h, --help           show this help message and exit<br/>
  --attach ATTACH      Add Attachment [Ex. --attach "/root/Desktop/mail.csv"]<br/>
<br/>
Required Arguments:<br/>
  --list LIST          Emails List Location [Ex. --list "/root/Desktop/mails.txt"]<br/>
  --name NAME          Email Sender_Name [Ex. --name "firstname lastname"]<br/>
  --email EMAIL        Sender Email Address [Ex. --email sender@example.com]<br/>
  --password PASSWORD  Sender Email Password [Ex. --password sender_password]<br/>
  --subject SUBJECT    Subject Content [Ex. --subject "Enter Subject Here"]<br/>
  --body BODY          Body Content Location [Ex. --body "/root/Desktop/body.txt"]<br/>
  <br/>
  
### Usage
#### Email Without Attachment
python3 bulk-email-sender.py --list /root/Desktop/email.txt --name "Your Name" --email senderemail@example.com --password sender_password --subject "Email Subject Here" --body /root/Desktop/body.txt

#### Email With Attachment
```bash
python3 bulk-email-sender.py --list /root/Desktop/email.txt --name "Your Name" --email senderemail@example.com --password sender_password --subject "Email Subject Here" --body /root/Desktop/body.txt --attach /root/Desktop/body.txt
```
  

