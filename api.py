import urllib2
import json
import pdb
import csv


#LOCU API key
locu_api = "add key to work"


master_arry = []




def locationSearch(location, category):
	api_key = locu_api
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key 
	locality = location.replace(' ','%20')

	final_url = url +  '&locality=' + locality + "&category=" + category
	
	help = urllib2.urlopen(final_url)

	json_data =  json.load(help)

	for items in json_data['objects']:
		print(items['name'].encode('ascii', 'ignore'),items['phone'].encode('ascii', 'ignore'),items['street_address'].encode('ascii', 'ignore'))
		master_arry.append([items['name'].encode('ascii', 'ignore'),items['phone'].encode('ascii', 'ignore'),items['street_address'].encode('ascii', 'ignore')])

		#csv.write(items['name'].encode('ascii', 'ignore'),items['phone'].encode('ascii', 'ignore'),items['street_address'].encode('ascii', 'ignore'))

	
	with open("data.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(master_arry)
		

print("Welcome to my Restaurant API")
x = raw_input("Please enter a city: ")
y = raw_input("Please enter a category ex: SPA, Restaurant, Gym: ")


print("Here are the restaurant in " + str(x))
locationSearch(x,y)

#print("Restaurants New York")
#locationSearch("New York")
#pdb.set_trace()
