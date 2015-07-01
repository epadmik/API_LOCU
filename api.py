import urllib2
import json
import pdb


locu_api = 'f087ffd8e0a495f6ac6f5df6885fca48d3c1e22b'
url = "https://api.locu.com/v1_0/venue/search/?api_key=f087ffd8e0a495f6ac6f5df6885fca48d3c1e22b"




def locationSearch(location):
	api_key = locu_api
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key 
	locality = location.replace(' ','%20')

	final_url = url +  '&locality=' + locality + "&category=restaurant"
	
	help = urllib2.urlopen(final_url)

	json_data =  json.load(help)

	for items in json_data['objects']:
		print(items['name'],items['phone'])
		


#x = input("Please enter a city")
print("Restaurant LA")
locationSearch("Los Angles")
print("Restaurants New York")
locationSearch("New York")
#pdb.set_trace()
