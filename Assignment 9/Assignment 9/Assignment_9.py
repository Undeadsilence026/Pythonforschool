#Assignment 9 file transfer

import os
import time
import logging

def chooseDir():
	print("This is your current file directory "+os.getcwd())
	time.sleep(2)
	print("Is there another file directory would you like to use?\nIf not copy and paste the current directory.")
	time.sleep(2)
	print("Remember that file directories are case sensitive")
	user_input = input()
	answer = input("Is this the file directory you want? "+user_input+"\n")
	#os.chdir(user_input)
	if answer == 'yes' or answer == 'y':
		os.chdir(user_input)
		pass
	else:
		print("Enter the correct file directory")
		user_input = input()
		os.chdir(user_input)

def creatingFiles():
	print("Create a new folder to place your text in")
	time.sleep(2)
	print("Remember that files can also be case sensitive")
	user_input2 = input()
	print("Creating Folder "+user_input2)
	os.mkdir(user_input2)
	os.chdir(user_input2)
	#logging.basicConfig(filename=user_input2, level=logging.DEBUG)

def loggingData():
	print("Please log your first and last name")
	time.sleep(2)
	print("Address")
	time.sleep(2)
	print("And Phone Number")
	name = input()
	address = input()
	phoneNumber = input()
	print("You have entered\n"+name+'\n'+address+'\n'+phoneNumber)
	answer2 = input("Is this information correct\n")
	if answer2 == 'yes' or answer2 == 'y':
		pass
	else:
		print("Please enter the correct information")
		name = input()
		address = input()
		phoneNumber = input()
		print("You have entered\n"+name+'\n'+address+'\n'+phoneNumber)
	user_input3 = input("What is the name of the file your placing the text in?\n")
	logging.basicConfig(filename=user_input3+".txt", level=logging.DEBUG)
	logging.debug(name)
	logging.debug(address)
	logging.debug(phoneNumber)

tryAgain = 'yes'
while tryAgain == 'yes' or tryAgain == 'y':
	chooseDir()
	creatingFiles()
	loggingData()
	print("Would you like to try again? (yes/no)")
	tryAgain = input()
	if tryAgain == 'no':
		print("Thank you for logging your information")