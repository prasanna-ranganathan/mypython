#!/usr/bin/env python

import imaplib

mailserver = imaplib.IMAP4_SSL('imap.outlook.com',993)
username = "prasanna78@live.com"
password = "vershini.a"
mailserver.login(username,password)

status,count = mailserver.select('Inbox')
status,data = mailserver.fetch(count[0],'(UID BODY[TEXT])')

print data[0][1]

mailserver.close()
mailserver.logout()

