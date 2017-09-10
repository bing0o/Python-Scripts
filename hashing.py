#!/usr/bin/env python

import hashlib
from optparse import *


class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()

print(cl.blue+"""

	*--------------------------------------*
	|       programmed by : mohamed        |
	|           fb.me/hack1lab             |
	*--------------------------------------*
	   _                _    _       _     
	  | |__   __ _  ___| | _| | __ _| |__  
	  | '_ \ / _` |/ __| |/ / |/ _` | '_ \ 
	  | | | | (_| | (__|   <| | (_| | |_) |
	  |_| |_|\__,_|\___|_|\_\_|\__,_|_.__/ 
	
	                 hashing
	                ---------

"""+cl.end)

def hashing(data, type_h):
	hash_type = hashlib.new(type_h)
	hash_type.update(data)
	return hash_type.hexdigest()

parser = OptionParser("""

-------------------------[Usage]------------------------

#Options:
	
	-x    hashing text 
	-f    hashing file  any file e.g (.txt, .rar, .zip, .iso, .exe, .py, ........ etc)
	-t    the Hashing type  e.g (md5, md4, sha1, sha256, sha512, ....... etc)
	
#Example:

	python hashing.py -x hacklab -t md5

	python hashing.py -f kali_linux.iso -t sha1

		""")
try:
	parser.add_option("-x",dest="Text",type="string", help="enter text for hashing")
	parser.add_option("-f",dest="File",type="string", help="enter file for hahsing")
	parser.add_option("-t",dest="Type",type="string", help="Enter the Hashing type")
	(options, args) = parser.parse_args()
	if options.Text == None and options.File == None:
		print(cl.blue+parser.usage+cl.end)
		exit(0)
	else:
		Text = str(options.Text)
		File = str(options.File)
		Type = str(options.Type)
		if options.Text == None:
			read_file = open(File, 'r')
			File = str(read_file.read())
			result = hashing(File, Type)
			print(cl.red+"[+] Hash File: [ "+result+' ]'+cl.end+'\n')
		elif options.File == None:
			result = hashing(Text,Type)
			print(cl.red+"[+] Hash Text: [ "+result+' ]'+cl.end+'\n')
		else:
			print(cl.blue+"[-] there error !!"+cl.end)
except Exception, e:
	print("Error: "+ str(e))
