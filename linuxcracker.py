#!/usr/bin/env python

import crypt, sys

def cracker(passcrypt, dicfile):
	dicfile = open(dicfile, 'r')
	for word in dicfile:
		password = word.strip('\n')
		cryptword = crypt.crypt(password, passcrypt)
		if cryptword == passcrypt:
			print("\n[+]Password Found: "+word)
			return True

	print("[-]Not Found!")

try:
	filepass = sys.argv[1]
	dictfile = sys.argv[2]
except:
	print('#Usage:\n\tpython linuxcracker.py passfile.txt dictfile.txt')
	exit(0)

readpass = open(filepass, 'r')

for line in readpass:
	user = line.split(':')[0]
	cryptpass = line.split(':')[1].strip(' ')
	print("[*] Cracking | User: "+user)
	cracker(cryptpass, dictfile)

