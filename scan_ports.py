#!/usr/bin/env python

import socket
import time
from optparse import *

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()


print (cl.blue+"""

	*--------------------------------------*
	|      programmed by : mohamed         |
	|          fb.me/hack1lab              |
	|         fb.me/mohamed1lar            |
	*--------------------------------------*
	   _                _    _       _     
	  | |__   __ _  ___| | _| | __ _| |__  
	  | '_ \ / _` |/ __| |/ / |/ _` | '_ \ 
	  | | | | (_| | (__|   <| | (_| | |_) |
	  |_| |_|\__,_|\___|_|\_\_|\__,_|_.__/ 
	
	              Happy Hacking               
	            ----------------        
	            
"""+cl.end)

def scan(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip,port)):
		return None
	else :
		try:
			time.sleep(0.5)
			service = socket.getservbyport(port)
			print ("{}/tcp   {}".format(port,service))
		except socket.error:
			print ("{}/tcp   {}".format(port,"Unknown"))
			return True

parser = OptionParser("""

#Usage:
	
	python scan.py -t <Target Ip>


""")
parser.add_option("-t",dest="target",type="string")
(options, args) = parser.parse_args()
if options.target == None:
	print(parser.usage)
	exit(0)
else:
	target = str(options.target)
	print cl.red+"\n[+] Start scanning >> ", target +cl.end+ "\n"
	ports = range(65535)
	for port in ports:
		scan(target,port)
print("\n\t * Good bye *\n")