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

\t     _ _      _                _       
\t  __| (_)_ __| |__  _ __ _   _| |_ ___ 
\t / _` | | '__| '_ \| '__| | | | __/ _ \\
\t| (_| | | |  | |_) | |  | |_| | ||  __/
\t \__,_|_|_|  |_.__/|_|   \__,_|\__\___|"""+bold+"V: 1.5"+ end +blue+"""
\t
\t             Coded by: Bingo
\t             ---------------
"""+end)


from concurrent.futures import ThreadPoolExecutor as executor
import sys, time, requests


start = time.time()
count = 0

def printer(word):
	sys.stdout.write(word + "                                        \r")
	sys.stdout.flush()
	return True


def presearch(domain, ext, url):
	if ext == 'Null':
		checkstatus(domain, url)
	elif url == "" or url == " ":
		pass
	else:
		ext = list(ext)
		ext.append("")
		for i in ext:
			if i == "":
				link = url
			else:
				link = url + "." + str(i)
			
			checkstatus(domain, link)


def checkstatus(domain, url):
	if url == "" or url == " ":
		pass
	elif url.startswith("#"):
		pass
	elif len(url) > 30:
		pass

	else:
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
				#link = req.url
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
	print(red + "#Usage:\n\tpython dirbrute.py <Wordlist> <Domain> <Thread (optional)> <extensions (optional)>\n" + end)
	exit(0)

try:
	thread = sys.argv[3]

except:
	thread = 20

try:
	ext = sys.argv[4]
	#ext = list(ext)
except:
	ext = "Null"

#print(ext)


if domain.startswith("http"):
	domain = domain
else:
	domain = "http://" + domain

if domain.endswith("/"):
	domain = domain
else:
	domain = domain + "/"




lines = len(open(urlsfile, encoding="utf-8").readlines())

print("["+ yellow + bold +"Info"+ end +"]:\n")
print(blue + "["+red+"+"+blue+"] Target: " + end + domain)
print(blue +"["+red+"+"+blue+"] File: " + end + urlsfile)
print(blue +"["+red+"+"+blue+"] Length: " + end + str(lines))
print(blue +"["+red+"+"+blue+"] Thread: " + end + str(thread))
print(blue +"["+red+"+"+blue+"] Extension: " + end + str(ext))
print("\n["+ yellow + bold +"Start Searching"+ end +"]:\n")

#exit(0)

urls = open(urlsfile, 'r')

if ext == "Null":
        pass

else:
        ext = ext.split(",")



with executor(max_workers=int(thread)) as exe:
	jobs = [exe.submit(presearch, domain, ext, url.strip('\n')) for url in urls]
	#results = [job.result() for job in jobs]
	
#print('\n'.join(results))


print(red+"Took: "+end, time.time() - start, "                          \r")

print("\n\t* Happy Hacking *")

