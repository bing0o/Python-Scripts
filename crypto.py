#!/usr/bin/python

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from optparse import *



class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()



print(cl.red+"""                           
\t           
\t                |    
\t                |
\t           ------------        -----------
\t                |
\t                |
\t    )                                           (  
\t    \ \                                       / /
\t     \ |\                                   / |/ 
\t      \|  \            hacklab            /   /   
\t       \   |\          -------          / |  /  
\t        \  |  \_______________________/   | /  
\t         \ |    |      |      |      |    |/ 
\t          \|    |      |      |      |    /
\t           \____|______|______|______|___/


# fb.me/hack1lab
# fb.me/mohamed1lar

"""+cl.end)



parser = OptionParser("""

#Usage:

	-e   file to encryption
	-d   file to decryption
	-p   password to encryption or decryption

#Example:
	
	python crypto.py -e <File To Encrypt> -p <Password>

	python crypto.py -d <File To Decrypt> -p <Password>


""")

def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = "hacklab."+filename
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
	chunksize = 64 * 1024
	outputFile = filename.split('hacklab.')[1]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)

def getkey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()

def Main():
	parser.add_option("-e",dest="en",type="string", help="enter file to encryption")
	parser.add_option("-d",dest="de",type="string", help="enter file to decryption")
	parser.add_option("-p",dest="password",type="string", help="enter password")
	(options, args) = parser.parse_args()
	if options.en == None and options.de == None:
		print(cl.blue+parser.usage+cl.end)
		exit(0)
	else:
		en = str(options.en)
		de = str(options.de)
		password = str(options.password)
		if options.de == None:
			encrypt(getkey(password), en)
			os.remove(en)
			print(cl.red+"\n\t* Done *"+cl.end)
		elif options.en == None:
			decrypt(getkey(password), de)
			os.remove(de)
			print(cl.red+'\n\t* Done *'+cl.end)
		else:
			print("Oops operation failed")


if __name__ == '__main__':
	Main()