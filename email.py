#! /usr/bin/python
# This emails the RPi IP information on.
# Add to /etc/rc.local to run at boot.
# Write 'sleep 20' before script in rc.local.

import os
import smtplib
#import creds
import re

ip_regex = '(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/[0-3][0-9]|(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
gmail_user = 'bowlofrichards@gmail.com'
gmail_pw = 'Mu5hr00mT1p'
recvr = 'kevin.bush@nexusis.com'

ipconf = os.popen('ipconfig').read()
#ip_add = re.findall(ip_regex, ipconf)

header = "To: " + recvr + "\n" + "From: " + gmail_user + "\n" + "Subject: Current RPi IP is: " + ip_add[0]
msg = header + "\n\n" + "Full ipconfig output:" + "\n" + ipconf

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pw)

print msg

smtpserver.sendmail(gmail_user, recvr, msg)

print "\n" + "Done!" + "\n"

smtpserver.close()
