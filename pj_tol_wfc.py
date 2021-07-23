import requests 
import os
import pprint



app_id = os.environ["TL_PRIMARY"]
app_key = os.environ["TL_SECONDARY"]
url_append = f'?app_id={app_id}&app_key={app_key}' 

# print(url_append)
# print('KEY OK')

# URL
url = "https://api.tfl.gov.uk/AirQuality"

# We send the request to the API
# NOTE: if you don't have your APP_KEY, run this without the url_append
res = requests.get(url+url_append)

# print(res.status_code)

## from IPython.display import JSON
res_j = res.json()

for sub_list in res_j['currentForecast']:
    if sub_list['$id']=='3':  # '3' means tomorrow
         print('Tomorrow air pollution forecast',':',sub_list['forecastSummary'])



exit()

