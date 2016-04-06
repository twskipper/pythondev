#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
sender = '363103397@qq.com'
receiver = '97662036@qq.com'
subject = 'python email test'
smtpserver = 'smtp.qq.com'
username = '363103397@qq.com'
password = 'Lian5337.'
 
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('mixed')
msg['Subject'] = "Link"
 
# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = """\
 
  
Hi!
 
       How are you?
 
       Here is the <a href="http://www.python.org">link</a> you wanted.
 
  
 
"""
 
# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
 
# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
att = MIMEText(open('/Users/skipper/Pictures/1.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msg.attach(att)
 
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
