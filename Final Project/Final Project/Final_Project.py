#Final Project
#import request and json libraries
import json
import requests
import time

#Make a variable for api, website, and combined
api_key = '&appid=717eecd822dd2b524596ca734d886b22'
base_url = 'https://api.openweathermap.org/data/2.5/weather?'

#display welcome message
def displayIntro():
	print("Hello and welcome to the weather finder")
	time.sleep(2)
	print("Would you like to enter a zipcode or city/state")


#ask for zipcode or city/state
def location():
	user_input = input()
	time.sleep(2)
	print("Where are you from?")
	#if user wants zipcode
	if user_input == 'zipcode':
		zipCode = input("What is your zipcode?")
		zip_url = base_url+'&zip='+zipCode+api_key+'&units=imperial' #zip underscore code is user input
		weather_data = requests.get(zip_url)
		r_dict = weather_data.json()
		print(r_dict['main.temp'+'\n'+'weather.main'+'\n'+'main.humidity'+'\n'+'wind.speed'+'\n'+'name'])
	#if user wants city/state
	elif user_input == 'city/state':
		cityName = input("What is the city name?")
		stateSymbol = input("What is the state?")
		city_url = base_url+'q='+cityName+','+stateSymbol+api_key+'&units=imperial'
		weather_data = requests.get(city_url)
		r_dict = weather_data.json()
		print(r_dict['main.temp'+'\n'+'weather.main'+'\n'+'main.humidity'+'\n'+'wind.speed'+'\n'+'name'])
	#if user didnt type anything right
	else:
		print("This is not a location were looking for")
		time.sleep(2)
		print("Please type the right location")
		pass

#Call all functions
tryAgain = 'yes'
while tryAgain == 'yes' or tryAgain == 'y':
	displayIntro()
	location()
	print("Would you like to see the weather for another city?")
	tryAgain = input()
	if tryAgain == 'no':
		print("Thank you for using the Weather Finder")
	


