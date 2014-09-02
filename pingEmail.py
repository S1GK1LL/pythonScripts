#script to ping an address and email you when it doesnt respond.


import subprocess
import time
import datetime
import os
import re
import smtplib

targetIP = raw_input("Enter url or IP Address:\n> ")

while True:
		time.sleep(3)
                ping = subprocess.Popen(["ping", "-n", "1", targetIP], stdout=subprocess.PIPE).stdout.read()
		date2 = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
		#print (ping)
                if 'Reply from' in ping:
					print "\npinging..............................\n"
					print "successful ping! %s is up. %s\n" % (targetIP, date2)
                else:
					ip_regex = '(?:[0-9]{1,3}\.){3}[0-9]{1,3}\/[0-3][0-9]|(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
					gmail_user = 'bowlofrichards@gmail.com'
					gmail_pw = 'Mu5hr00mT1p'
					recvr = 'kevin.bush@nexusis.com'

					ipconf = os.popen('ipconfig').read()
					ip_add = re.findall(ip_regex, ipconf)

					header = "To: " + recvr + "\n" + "From: " + gmail_user + "\n" + "Subject: VPN is down! " + targetIP#[0]
					msg = header + "\n\n" + "Current Media Server IP is:" + "\n" + ipconf

					smtpserver = smtplib.SMTP("smtp.gmail.com",587)
					smtpserver.ehlo()
					smtpserver.starttls()
					smtpserver.ehlo
					smtpserver.login(gmail_user, gmail_pw)

					print msg

					smtpserver.sendmail(gmail_user, recvr, msg)

					print "\n" + "Done!" + "\n"

					smtpserver.close()
					break
					#continue
