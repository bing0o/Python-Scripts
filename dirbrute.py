#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  subchecker.py
#  
#  Copyright 2019 bingo <bingo@hacklab>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  

yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
red = "\033[91m"
bold = "\033[1m"
end = "\033[0m"


print(blue+bold+"""
     _ _      _                _       
  __| (_)_ __| |__  _ __ _   _| |_ ___ 
 / _` | | '__| '_ \| '__| | | | __/ _ \
| (_| | | |  | |_) | |  | |_| | ||  __/
 \__,_|_|_|  |_.__/|_|   \__,_|\__\___|"""+red+"V: 1.5"+blue+"""
 
                   Coded by: Bingo
                   ---------------

	"""+end)


from concurrent.futures import ThreadPoolExecutor as executor
from threading import Lock
import sys, time, requests


start = time.time()


def printer(word):
	sys.stdout.write(word + "                                        \r")
	sys.stdout.flush()
	return True


def checkstatus(domain, url):
	printer("Testing: " + domain + url)
	#time.sleep(1)
	try:
		link = domain + url
		req = requests.head(link)
		st = str(req.status_code)
		if st.startswith("2"):
			print(green + "[+] 200 | Found: " + end + "[ " + url + " ]" + "                                                   \r")
		elif st.startswith("3"):
			link = req.headers['Location']
			link = req.url
			print(yellow + "[*] "+st+" | Redirection From: " + end + "[ " + url + " ]" + yellow + " -> " + end + "[ " + link + " ]" + "                                         \r")

		#writer(link,'up')
		
		return True
		
	except Exception:
		#writer(url,'down')
		return False


try:
	urlsfile = sys.argv[1]#raw_input("[subdomains]> ")
	domain = sys.argv[2]

except Exception:
	print(blue + "#Usage:\n\tpython subchecker.py <paths file> <domain>\n" + end)
	exit(0)


urls = open(urlsfile, 'r')


with executor(max_workers=20) as exe:
	jobs = [exe.submit(checkstatus, domain, url.strip('\n')) for url in urls]
	#results = [job.result() for job in jobs]
	
#print('\n'.join(results))


print("Took: ", time.time() - start)

print("\n\t* Happy Hacking *")

