import requests 
import os
# don't forget package os
app_id = os.environ["TL_PRIMARY"]
app_key = os.environ["TL_SECONDARY"]
url_append = f'?app_id={app_id}&app_key={app_key}' 

url = "https://api.tfl.gov.uk/BikePoint/"
res = requests.get(url+url_append)
res_j = res.json()

import pprint

# pprint.pprint(res_j)

s_nbD=0
s_nbB=0
s_nbE=0
# print(type(s_nbE))
tot_bp=len(res_j)
# print(tot_bp)
for i in res_j:
    b_all=['bid' , i['id']]
    for j in i['additionalProperties']:  # 9 rows
        if (j['key']) == 'NbDocks':
            s_nbD= s_nbD +  int((j['value']))
        elif (j['key']) == 'NbBikes': 
            s_nbB= s_nbB + int((j['value']))
        elif (j['key']) == 'NbEmptyDocks':   
             s_nbE= s_nbE +   int((j['value']))
             #s_nbE=[j['key'], j['value']]
             #print(j['key'], j['value'])
    #s2_bk_lst= [b_all, s_nbD,  s_nbB, s_nbE ]
    #print(s2_bk_lst)
print('Total location of BikePoints: ' + str(tot_bp), '\n'
     'Total Docks: ' + str(s_nbD), '\n'
     'Total Empty Docks: ' + str(s_nbE), '\n'
     'Total Full  Docks: ' + str(s_nbB), '\n'
     )


exit()
