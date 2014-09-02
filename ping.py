#Script will continuosly ping an IP with a 3 second interval and timestamp the output.

import subprocess
import time
import datetime

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
					print "\nping failure! %s VPN is down! %s\n" % (targetIP, date2)
					continue
