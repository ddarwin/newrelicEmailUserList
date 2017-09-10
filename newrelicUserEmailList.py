import json
import requests

pageNum = 1

# Output CSV file 
download_dir = "newrelicUserEmailList.csv" 

csv = open(download_dir, "w") 
url = 'https://api.newrelic.com/v2/users.json?page=1'

# HTTP Request headers dictionary. Include additional request headers here
head = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Api-Key':'<Add_REST_API_Key_HERE>' 	# Default REST API Key
}

# HTTP Request parameters dictionary. Include additional request parameters here
parms = {
    'page':  1
}

# Ask the user for the New Relic REST API Key for the account or hit enter to use default
restKey = input("Enter the REST API for the New Relic account or hit enter for default\n")

if restKey != '':    #User entered Key
	# print("REST Key =",restKey)
	head['X-Api-Key'] = restKey
	

userCount = 0 # Loop iterator

# Infinite loop to support paginated REST API
while True:
	
	# Call the Users REST API
	r = requests.get(url, headers=head)

	# Test for response status code of 200 or 300 (probably add more later)
	if r.status_code != 200 and r.status_code != 300:
		print("The REST API returned status code", r.status_code)
		break
	else:
		
		# Iterate through the users and write to the CSV output file.
		for user in r.json()["users"]:
			userCount = userCount + 1
			if userCount > 1 :
				csv.write(",") # Add separator

			# Write user email to file
			csv.write(user["email"])
		
		# Pagination - if there is a "next" link, update URL and read next page	
		try:
			url = r.links['next']['url']
		except KeyError:						# If there is no "next" link
			break
			
print("Total user emails:", userCount)
			
		
