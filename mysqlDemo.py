#!/usr/bin/enu python 

import MySQLdb

db = MySQLdb.connect(host='localhost',user='root',passwd='prasanna',db='super_market')

cur = db.cursor()

cur.execute("Select * from employees")

for row in cur.fetchall():
  print row

db.close()
