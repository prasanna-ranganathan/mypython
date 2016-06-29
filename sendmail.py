#!/usr/bin/env python


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import getpass

toaddr = "prassanna.mit@gmail.com"
fromaddr = "prasanna78@live.com"
text = "test message sent form python"
username = "prasanna78@live.com"
password = "vershini.a"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.outlook.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr,toaddr,msg.as_string())
server.quit()

