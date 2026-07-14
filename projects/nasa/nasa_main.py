import requests
import matplotlib as plt

# Call the API and store the response
url = 'https://api.nasa.gov/DONKI/CME?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=DEMO_KEY'
r = requests.get(url)
print("Status code: ", r.status_code)
response_dict = r.json()

# Process information
res_dict = response_dict['items']

for res_dict in response_dict:
    print("\nInformation about recennt CMEs")
    print("ActivityID: ", response_dict['activityID'])
