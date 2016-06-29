#!/usr/bin/env python

import poplib

username="393972"
password="Jan-2016"
mail_server = "mail.cognizant.com"

p = poplib.POP3_SSL(mail_server)
p.user(username)
p.pass_(password)
for msg_id in p.list()[1]:
  print msg_id
  outf = open('%s.email' % msg_id, 'w')
  outf.write("\n".join(p.retr(msg_id)[1]))
  outf.close()
p.quit()

