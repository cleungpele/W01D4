import requests 
import os
# don't forget package os
app_id = os.environ["TL_PRIMARY"]
app_key = os.environ["TL_SECONDARY"]

r_id='Victoria'
r_direction='all'
#s_type='regual'
#url_append = f'?app_id={app_id}&app_key={app_key}&serviceTypes{s_type}' 


url_append = f'?app_id={app_id}&app_key={app_key}' 
url_1 = "https://api.tfl.gov.uk/Line"
url_2 = f'/{r_id}/Route/Sequence/{r_direction}'
url=url_1 + url_2
res = requests.get(url+url_append)
res_j = res.json()

#print (url+url_append)

import pprint

print(len(res_j))
# pprint.pprint(res_j)
print('Victoria has', str(len(res_j)) , 'stations')

exit()
