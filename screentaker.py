#!/usr/bin/python

blue = "\033[94m"
red = "\033[91m"
bold = "\033[1m"
end = "\033[0m"

print(blue+bold+"""
 ____      _____     _
/ ___|  __|_   _|_ _| | _____ _ __
\___ \ / __|| |/ _` | |/ / _ \ '__|
 ___) | (__ | | (_| |   <  __/ |
|____/ \___||_|\__,_|_|\_\___|_|
                                                       
        Coded by: Bingo                                   
        ---------------

	"""+end)



from selenium import webdriver
import sys, time, requests

f = open('/dev/null', 'w')
sys.stderr = f

try:
	driver = webdriver.PhantomJS()
except:
	pass


def printer(url):
	sys.stdout.write("[+] "+url+"                                                            \r")
	sys.stdout.flush()
	return True


def takescreen(link):
	printer(link)
	driver.get(link)
	name = link.split('/')[2]
	#time.sleep(2)
	if link.startswith('https'):
		driver.save_screenshot('https-'+name+'.png')
	else:
		driver.save_screenshot('http-'+name+'.png')
	
	return True


def check(url):
	try:
		req = requests.get(url, timeout=10)
		scode = str(req.status_code)
		#print("status code: "+scode)
		if scode.startswith("2") or scode.startswith("3") or scode.startswith("4"):
			takescreen(url)
			return True
		else:
			return False
	except:
		return False

try:
	urlsfile = sys.argv[1]#raw_input("[subdomains list]> ")
except Exception:
	print("#Usage:\n\tpython subchecker.py <subdomains list>\n")
	driver.close()
	exit(0)
urls = open(urlsfile, 'r')

protocols = ['http://','https://']

for url in urls:
	for protocol in protocols:
		url = url.strip('\n')
		link = protocol + url
		check(link)
driver.close()