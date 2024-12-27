#This is a computerized version of the ceaser cipher wheel which was used during the world war
#Author:HackexDeCodebreaker
#Date:December 15,2024
#Lincence:BSD

import pyperclip
import time
import colorama
from colorama import Fore
import os

os.system('clear')
os.system('figlet "                  XcyberCrypt"')

message=input("Message>>>>")

translated=""
#setting up the key
key=input("Enter key>>>")
key=int(key)

LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-][}{|\":;\'\\,./<>?~`"

mode=input("Enter the mode>>>>")
mode=mode.lower()
for symbol in message:
	#get the encryption or decryption key for the message
	if symbol in LETTERS:
		num=LETTERS.find(symbol) #Get the number for the symbol
		if  mode=="encrypt":
			num=num+key
		elif mode=="decrypt":
			num=num-key
		if num >= len(LETTERS):
			num=num-len(LETTERS)
		elif num <0:
			num=num+len(LETTERS)
		translated=translated+LETTERS[num]
		print (translated)
		time.sleep(0.1)
	else:
	#Just add the symbol without encrypting or decryption
		translated=translated+symbol
		print (translated)
print (translated)
pyperclip.copy(translated)

