#!/usr/bin/python

blue = "\033[94m"
red = "\033[91m"
bold = "\033[1m"
end = "\033[0m"

print(blue+bold+"""
 ____        _      ____ _               _             
/ ___| _   _| |__  / ___| |__   ___  ___| | _____ _ __ 
\___ \| | | | '_ \| |   | '_ \ / _ \/ __| |/ / _ \ '__|
 ___) | |_| | |_) | |___| | | |  __/ (__|   <  __/ |   
|____/ \__,_|_.__/ \____|_| |_|\___|\___|_|\_\___|_|   
                                                       
                   Coded by: Bingo                                   
                   ---------------

	"""+end)



from selenium import webdriver
import urllib2, sys, time

try:
	driver = webdriver.PhantomJS()
except:
	pass

def takescreen(link):
	driver.get(link)
	name = link.split('/')[2]
	time.sleep(2)
	driver.save_screenshot(name+'.png')
	return True



def checkstatus(url):
	sys.stdout.write("Testing: "+url+"                                               \r")
	sys.stdout.flush()
	#print("Testing: "+url)
	try:
		r = urllib2.urlopen(url, timeout=1)

		print red+'[+] Found Site On: ' + end + url
		sys.stdout.write("[*] Taking ScreenShot......."+"                                  \r")
		sys.stdout.flush()
		takescreen(url)
		return True

			
	except Exception:
		pass

try:
	urlsfile = sys.argv[1]#raw_input("[subdomains list]> ")
except Exception:
	print("#Usage:\npython subchecker.py <subdomains list>\n")
	exit(0)
urls = open(urlsfile, 'r')

protocols = ['http://','https://']

for url in urls:
	for protocol in protocols:
		url = url.strip('\n')
		link = protocol + url
		checkstatus(link)
