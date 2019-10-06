#!/usr/bin/env python

import requests, sys

class wayback():
	def __init__(self, url, limit):
		self.url = "https://web.archive.org/cdx/search?url="+url+"&matchType=prefix&collapse=urlkey&output=text&fl=original&\
		filter=&limit="+str(limit)

	def get(self):
		headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/68.0"}
		r = requests.get(self.url, headers=headers)
		results = r.text
		return results


def main():
	if len(sys.argv) < 3:
		print("[+] Usage:\n\tpython wayback.py <example.com> <limit number>")
		exit(0)

	url = sys.argv[1]
	limit = sys.argv[2]

	get = wayback(url, limit)
	res = get.get()

	for i in res.split():
		print(i)

if __name__=='__main__':
	main()