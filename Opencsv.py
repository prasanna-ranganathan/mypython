#!/usr/bin/env python

import csv

Email = []

with open('attendies.csv') as f:
  csv_f = csv.reader(f)
  for row in csv_f:
    Email.append(row[2])

  print Email,"TOtal emails:",len(Email)
