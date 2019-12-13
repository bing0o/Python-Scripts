#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor as executor
import socket
import time
import sys

blue = "\033[94m"
red = "\033[91m"
end = "\033[0m"

start = time.time()

print(blue+"""
 ____            _   ____                  
|  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | |
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|
                By: @bing0o
"""+end)


def printer(shit):
	sys.stdout.write(shit+"               \r")
	sys.stdout.flush()
	return True


def scan(ip,port,l):
	printer("Testing Port: "+str(port))
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	space = 10 - l
	space = " " * space
	if s.connect_ex((ip,port)):
		return None
	else :
		try:
			service = socket.getservbyport(port)
			print(str(port) + "/TCP" + space + service)
		except socket.error:
			print(str(port) + "/TCP" + space + "Unknown")

		except KeyboardInterrupt:
			print("[-] Exiting!")
			exit(1)

	return True

parser = ("""
#Usage:
	
	python scan.py <Target Ip/Host> <Threads, (default: 10)>
""")

try:
	target = sys.argv[1]
except:
	print(parser)
	exit(1)

try:
	thread = sys.argv[2]
except:
	thread = 10

print(red+"[+] Target: "+end+target)
print(red+"[+] Threads: "+end+str(thread))
print(red+"[+] Start The Scan\n"+end)
print("PORT          SERVICE")
print("----          -------")
ports = range(65535)
try:
	with executor(max_workers=int(thread)) as exe:
		[exe.submit(scan, target, port, len(str(port))) for port in ports]
except KeyboardInterrupt:
	print("[-] Exiting!")
	exit(1)


took = time.time() - start
took = took / 60
took = round(took, 2)

print("                            \r")
print(blue+"[+] Took: "+end+str(took)+"           ")
