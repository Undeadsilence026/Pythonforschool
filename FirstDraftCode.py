#first draft of final project
#import request and json libraries
import json
#import requests
import time

#Make a variable for api, website, and combined
api_key = '&appid=717eecd822dd2b524596ca734d886b22'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'
#zip_url = base_url+'&zip='+zipCode #zip underscore code is user input
#city_url = base_url+'q='+cityName+','+stateSymbol
#weather_data = requests.get(final_url).json()

#display welcome message
def displayIntro():
	print("Hello and welcome to the weather finder")
	time.sleep(2)
	print("Where are you from?")
	time.sleep(2)
	print("Would you like to enter a zipcode or city/state")
	user_input = input()

#ask for zipcode or city/state
def location():
	if user_input == 'zipcode':
		zipCode = input("What is your zipcode?")
		display()
	elif user_input == 'city/state':
		cityName = input("What is the city name?")
		stateSymbol = input("What is the state?")
		print(city_url)
	else:
		print("This is not the location were looking for")
		time.sleep(2)
		print("Please type the right location")