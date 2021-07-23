import requests 
import os
import pprint


import requests 
import os
# don't forget package os
app_id = os.environ["TL_PRIMARY"]
app_key = os.environ["TL_SECONDARY"]
url_append = f'?app_id={app_id}&app_key={app_key}' 

url = "https://api.tfl.gov.uk/Journey/Meta/Modes"
       #https://api.tfl.gov.uk/Mode/ActiveServiceTypes
res = requests.get(url+url_append)

res_j = res.json()

#print(url_append)
#print(url)
#print(res_j)
import pprint

#pprint.pprint(res_j)


# print(len(res_j))
o_type=[]
for i in res_j:
    if i['isTflService']:    # is ToL services
        #print(i['modeName'])
        need_mode=i['modeName']
        #print(type(need_mode))
        #print(type(o_type))
        o_type = o_type + [i['modeName']]
        #print(o_type)
        #print(type(o_type))
    
print (o_type)
print("Number of different modes of transport is:", len(o_type))

exit()
