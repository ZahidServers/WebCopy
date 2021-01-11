from urllib.request import urlopen
import re
import time
import os
import sys
from cfonts import render, say
os.system("title Website Track By Mohammed Zahid Wadiwale")
def clear():
	if name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def name():
	print(render('Website Track', colors=['red', 'yellow'], align='center', size=(120,18)))
	print(render('By Zahid', colors=['red', 'yellow'], align='center', size=(120,4)))
while True:
	name()
	try:
		url=input("\n Enter URL:")
		website = urlopen(url)
		try:
			html = website.read().decode("latin1")
		except:
			try:
				html = website.read().decode("utf-8")
			except:
				try:
					html = website.read().decode("latin2")
				except:
					print("Error Cant decode the Website")
					time.sleep(5)
					sys.exit()
		links = re.findall('"((http|ftp)s?://.*?)"', html)
		for link in links:
			print(link[0]+" "+link[1]+"\n", file=open("output.txt", "a"))
		for link in links:
			try:
				v= urlopen(link)
				i=0
				try:
					html2=website.read().decode("latin1")
				except:
					try:
						html2 = website.read().decode("utf-8")
					except:
						try:
							html2 = website.read().decode("latin2")
						except:
							print("\n")
							i=1
				if i==0:
					links2 = re.findall('"((http|ftp)s?://.*?)"', html2)
					for linkf in links2:
						print(linkf[0]+" "+linkf[1]+"\n", file=open("output.txt", "a"))
			except:
				print("\n")
		time.sleep(15)
	except:
		print("Error: Invalid URL")
		time.sleep(5)
	clear()