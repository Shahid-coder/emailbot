'''This is a simple email bot in which you can sent no. Of automatic  emails you want using python smtplib'''

import smtplib #built in modules

server=smtplib.SMTP("smtp.gmail.com",587)

server.starttls()#for starting tls

server.login("your-email","your-password")

i=0

while i<no_of_email: #no of emails you want to send

    i+=1

    server.sendmail("from","to","message")'''This is a simple email bot in which you can sent no. Of automatic  emails you want using python smtplib'''
