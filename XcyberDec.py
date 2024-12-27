#This  is a program to crack the caesar cipher with the bruteforcing technique
#Author:HackexDecodebreaker
#Github:HackexDeCodebreaker
#Lincence:BSD
#Date:December 16,2024

import pyperclip
import time
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message=input("Message>>>")

for key in range(len(LETTERS)):
	translated=''
	

	for symbol in message:
		if symbol in LETTERS:
			num=LETTERS.find(symbol)
			num=num-key
			

			if num<0:
				num=num+len(LETTERS)
			translated=translated+LETTERS[num]

		else:
			translated=translated+symbol
		print (translated)
		#time.sleep(0.1)
	print ('Key #%s:  %s' % (key,translated))
	time.sleep(0.1)
