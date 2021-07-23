import requests 
import os
# don't forget package os
app_id = os.environ["TL_PRIMARY"]
app_key = os.environ["TL_SECONDARY"]

s_from='Heathrow Airport'
g_to='Tower Bridge'
def serach_info(s_mode):
    url_append = f'?app_id={app_id}&app_key={app_key}&mode={s_mode}' 
    url_1 = "https://api.tfl.gov.uk/Journey/JourneyResults/"
    url_2 = '51.4700%2C%20-0.4543/to/51.5055%2C%20-0.075'
     
    url=url_1 + url_2
    #print(url)
    # url_append = f'?app_id={app_id}&app_key={app_key}&mode={s_mode}' 
    res =  requests .get(url+url_append)
    res_j = res.json()
    
#print(res.status_code)


    return(res_j)
     
res_j_tube=serach_info('tube')
res_j_bus=serach_info('bus')

# print(res.status_code)



import pprint



tube_dur=9999
for sub_list in res_j_tube['journeys']:
    #print(len(sub_list))
    for j in sub_list:
        #print(j)
        if j=='duration':
            if sub_list[j] < tube_dur:
                tube_dur= sub_list[j]
                #print(tube_dur)
            #print(sub_list[j])
#print(tube_dur)

bus_dur=9999
for sub_list in res_j_bus['journeys']:
    #print(len(sub_list))
    for j in sub_list:
        #print(j)
        if j=='duration':
            if sub_list[j] < bus_dur:
                bus_dur= sub_list[j]
                #print(tube_dur)
            #print(sub_list[j])
# print(bus_dur)


print('Total Tube Time: ', str(tube_dur))
print('Total Bus Time: ' , str(bus_dur) )


exit()
