import requests as re
import os


#r_pid=110119
r_pid='13955'
base = "https://api.themoviedb.org/3/"
#url = 'movie/popular'  #API method 
#url = '/genre/movie/list'  #API method 
#query_term = 'titanic'
url = f'person/{r_pid}'

api_key = os.environ["TMDB_API_KEY"]
# print(api_key)

endpoint = base + url #combining it together # 
print(endpoint)
res = re.get(endpoint,  #use endpoint and all the parameters we need in a dictionary
                     # params={'query': query_term, 'api_key': api_key})
                        params={ 'api_key': api_key})
res_j = res.json()


print(res.status_code)

print(len(res_j))

import pprint

pprint.pprint(res_j)

print('--------------- Output ------------')

print('Name:', res_j['name'] , '\n'
      'Date of birth:'  , res_j['birthday']   , '\n'
      'Place of birth:'       , res_j['place_of_birth']   , '\n'
      'Length of the biography:'       , res_j['biography']   
      )

exit()

