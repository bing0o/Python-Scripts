#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor as executor
import socket
import time
import sys
import argparse

green = "\033[32m"
bold = "\033[1m"
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
			print(red+"[-] Exiting!"+end)
			exit(1)

	return True




def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", help="Target IP/Host", type=str)
	parser.add_argument("-d", "--thread", help="threads number (Default 5)", type=int)
	parser.add_argument("-p", "--port", help="Ports range (Example: -p 20-1024)", type=str)
	args = parser.parse_args()

	target = str(args.target)
	thread = args.thread
	ports = str(args.port)

	if target == "None":
		parser.print_help()
		exit(1)
	if thread == None:
		thread = 5

	if ports == "None":
		ports = range(65535)
		p = "1-65535"
	else:
		try:
			p = ports
			ports = ports.split("-")
			ports = range(int(ports[0]), int(ports[1]))
		except IndexError:
			print("-p/--port, should be a range of ports, Example: -p 20-1024")
			exit(1)

	print(green+"[+] Target: "+end+target)
	print(green+"[+] Threads: "+end+str(thread))
	print(green+"[+] Ports: "+end+p)
	print(bold+"\n[+] Start The Scan\n"+end)
	print("PORT          SERVICE")
	print("----          -------")

	with executor(max_workers=int(thread)) as exe:
		try:
			[exe.submit(scan, target, port, len(str(port))) for port in ports]
		except KeyboardInterrupt:
			print(red+"[-] Exiting!"+end)
			exit(1)



	took = time.time() - start
	t = str(took).split('.')[0]
	m = int(t) / 60
	s = int(t) % 60
	
	print("                            \r")
	print(blue+"[+] Took: "+end+str(m)+":"+str(s))


if __name__ == '__main__':
	main()
