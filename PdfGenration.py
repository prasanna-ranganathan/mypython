#!/usr/bin/env python

from reportlab.pdfgen import canvas

def hello():
  string = ""
  c = canvas.Canvas("Grep.pdf")
  with open("Grep.py") as file:
    for line in file:
      string += line
  c.drawString(1000,1000,string)
  c.showPage()
  c.save()

hello()
