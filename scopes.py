#!/usr/bin/python3
#
# Python script to get the scope of Hackerone Private AND Public bug bounty programs
# Get your API token from: https://hackerone.com/settings/api_token/edit
# the program ID e.g Yahoo (https://hackerone.com/yahoo) is "yahoo" :D
#
# This script exclude IOS and Android assets.
#

import json,requests,argparse

class scope():
	def __init__(self, program, username, apikey):
		headers = {"Accept": "application/json"}
		url = 'https://api.hackerone.com/v1/hackers/programs/' + str(program)
		data = requests.get(url, headers=headers, auth=(username, apikey))
	
		p = json.loads(data.text)

		try:
			self.result = p['relationships']['structured_scopes']['data']
		except Exception:
			print("[!] Check Program ID, Your Username or Your Token and Try Again!")
			exit(1)

		self.count = len(self.result)


	def InScope(self):
		for i in range(self.count):
			if self.result[i]['attributes']['eligible_for_submission'] == False or str(self.result[i]['attributes']['asset_type']) == 'GOOGLE_PLAY_APP_ID' or str(self.result[i]['attributes']['asset_type']) == 'APPLE_STORE_APP_ID':
				continue
			else:
				print(self.result[i]['attributes']['asset_identifier'])


	def OutOfScope(self):
		for i in range(self.count):
			if self.result[i]['attributes']['eligible_for_submission'] == False:
				print(self.result[i]['attributes']['asset_identifier'])



def main():
	################ This is optional so you don't have to use -t AND -u Arguments.
	APIKEY = ""
	USERNAME = ""
	################
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", dest="token", type=str, help="Hackerone API Token.")
	parser.add_argument("-u", dest="username", type=str, help="Your Hackerone Username.")
	parser.add_argument("-p", dest="program", type=str, help="Hackerone Program ID.", required=True)
	parser.add_argument("-e", dest="exclude", help="Prints only out of scope assets", action='store_true')
	args = parser.parse_args()

	if APIKEY == "":
		apikey = str(args.token)
	else:
		apikey = APIKEY

	if USERNAME == "":
		username = str(args.username)
	else:
		username = USERNAME

	program = str(args.program)
	result = scope(program, username, apikey)

	if not args.exclude:
		result.InScope()
	else:
		result.OutOfScope()

if __name__ == '__main__':
	main()
