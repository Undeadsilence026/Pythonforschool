#Assignment 9 file transfer

import os
import time
import logging


def chooseDir():
	print("This is your current file directory "+os.getcwd())
	time.sleep(2)
	print("Is there another file directory would you like to use?")
	time.sleep(2)
	print("Remember that file directories are case sensitive")
	user_input = input()
	answer = input("Is this the file directory you want? "+user_input)
	os.chdir(user_input)
	if answer == 'yes' or answer == 'y':
		pass
	else:
		print("Enter the correct file directory")
		user_input = input()
		os.chdir(user_input)

def creatingFiles():
	print("Is there a specific file you would like to place your text in?")
	time.sleep(2)
	print("Would you like to create a new file?")
	time.sleep(2)
	print("Remember that files can also be case sensitive")
	time.sleep(2)
	#print("Use the format \Filename")
	user_input2 = input()
	print("Creating file "+user_input2)
	os.mkdir(user_input2)

def loggingData():
	print("Please log your first and last name")
	time.sleep(2)
	print("Address")
	time.sleep(2)
	print("And Phone Number")
	name = input()
	address = input()
	phoneNumber = input()
	print("You have entered "+name+' '+' '+address+' '+phoneNumber)
	answer2 = input("Is this information correct")
	if answer2 == 'yes' or answer2 == 'y':
		pass
	else:
		print("Please enter the correct information")
		name = input()
		address = input()
		phoneNumber = input()
	logging.basicConfig(filename=user_input2+'.txt', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
	logging.debug = name
	logging.debug = address
	logging.debug = phoneNumber

tryAgain = 'yes'
while tryAgain == 'yes' or tryAgain == 'y':
	chooseDir()
	creatingFiles()
	loggingData(creatingFiles)
	print("Would you like to try again? (yes/no)")
	tryAgain = input()
	if tryAgain == 'no':
		print("Thank you for logging your information")