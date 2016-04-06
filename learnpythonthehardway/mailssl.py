#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
sender = '363103397@qq.com'  
receiver = '1310342132@qq.com'  
subject = 'python email test'  
smtpserver = 'smtp.qq.com'  
username = '363103397@qq.com'  
password = 'rtynolanyiurbheb'  
content = """
hello,this mail from python by skipper
just test 
"""
msg = MIMEText(content)
msg['Subject'] = Header(subject, 'utf-8')  
print msg
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.qq.com')  
smtp.ehlo()  
smtp.starttls()  
smtp.ehlo()  
smtp.set_debuglevel(1)  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit() 
