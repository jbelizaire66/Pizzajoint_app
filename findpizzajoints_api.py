

# Homework #2
# findpizzajoints
# (c) 2017
# J.Belizaire (jbelizaire66) for OneMonth Python Course
# Take a location as input from user, then finds 'pizza joints' in a Radius (see below)
# It uses googleplaces API to find name, phone, url, and rating, etc. for each pizza joint.
# Pizza joints is defined as a pizza restaurant that is not a well known chain -
# - and has the word "pizza" in the business name.
# Enjoy!


#import googleplaces API
from googleplaces import GooglePlaces, types, lang
import os

#load my environment variables, and my secret keys
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


#---define my functions

#search a given location and radius and returns a list of pizza joints
def get_pizza_joint_list(alocation, search_radius):

	#get my private key from environment
	my_api_key = os.environ['MY_GAPI_KEY']	
	
	#set search radius
	#initialize API for use by all my functions
	google_places = GooglePlaces(my_api_key)

	# call Google Places API and search for Pizza places near a location
	query_result = google_places.nearby_search(
	        location=alocation, keyword='Pizza',
	        radius=search_radius, types=[types.TYPE_FOOD])
	
	#initialize pizza list
	pizza_joint_list = []

	#print (query_result)

	#if query_result.has_next_page_token:
	#	print("THERE ARE MORE PAGES")

	#fill list with dictionaries of pizza joints
	for pizza_place in query_result.places:
		#load details into place object; this is required for below
		pizza_place.get_details()

		#build a list with no pizza chains in it
		if not is_this_a_chain(pizza_place.name):
			#append dictionary to pizza joint list
			pizza_joint_list.append({"name": pizza_place.name,
				"rating": pizza_place.rating,
				"localphone": pizza_place.local_phone_number,
				"website": pizza_place.website
				})

	#2nd call to API, if there are more in the list, get some more names
	if query_result.has_next_page_token:
		query_result_next_page = google_places.nearby_search(
            pagetoken=query_result.next_page_token)

		for pizza_place in query_result_next_page.places:
			#get details into place object
			pizza_place.get_details()

			#remove the pizza chains from the list again
			if not is_this_a_chain(pizza_place.name):
				#append dictionary to pizza joint list
				pizza_joint_list.append({"name": pizza_place.name,
					"rating": pizza_place.rating,
					"localphone": pizza_place.local_phone_number,
					"website": pizza_place.website
					})

	#return the list of pizza joints
	return pizza_joint_list

#determines is a pizza joint is a chain based on the business name
def is_this_a_chain(pizza_joint_name):
	#pizza chain list
	pizza_chains = ["Domino's", "Pizza Hut", "Papa John's", "Little Caesars", "Chuck E. Cheese's"]

	for word in pizza_chains:
		if word.lower() in pizza_joint_name.lower():
			#print("FOUND THE STOP WORD")
			return 1	

#print all the mom and pop pizza joints 
def print_momandpop_pizza_list(pizza_joint_list):
	#keep a count of mom & pop joints
	number_of_joints = 0

	print ("-- HERE IS YOUR LOCAL MOM & POP PIZZA JOINT LIST --")
	
	#run through list and print dictionary
	for pizza_joint in pizza_joint_list:
		number_of_joints = number_of_joints + 1
		print("Name: {}" .format(pizza_joint["name"]))
		print("Rating: {}" .format(pizza_joint["rating"]))
		print("Phone: {}" .format(pizza_joint["localphone"]))
		print("Website: {} \n" .format(pizza_joint["website"]))
	print (">> WE FOUND {} JOINTS. THANK YOU! <<" .format(number_of_joints))



#----EXECUTE

#radius for search in (meters)
#search_radius = 8000 #(approximately 5 miles)

#get location from user as string
#search_location = input ("Welcome to the Find Pizza Joint service. (We hate pizza chains!) \nWhat's the location? ")

#print("Searching...\n")

#get the list of pizza joints and print them out				
#pizza_joints = get_pizza_joint_list(search_location, search_radius)

#print_momandpop_pizza_list(pizza_joints)

