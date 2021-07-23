import requests 
import os
# don't forget package os
app_id = os.environ["TL_PRIMARY"]
app_key = os.environ["TL_SECONDARY"]

def serach_info(s_mode):
    url_append = f'?app_id={app_id}&app_key={app_key}' 
    url_1 = "https://api.tfl.gov.uk/Line/Mode/"
    url_2 = f'{s_mode}/status'
    url=url_1 + url_2
    res = requests.get(url+url_append)
    res_j = res.json()
    return(res_j)

res_j_tube=serach_info('tube')
res_j_bus=serach_info('bus')


import pprint

#pprint.pprint(res_j_tube)

print('Total Bus Line: ', str(len(res_j_bus)))
print('Total Tune Line: ', str(len(res_j_tube)))
for i in res_j_tube:
    tube_name=i['name']
    print(tube_name)
    
# pprint.pprint(res_j_bus)


exit()
