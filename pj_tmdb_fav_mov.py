import requests as re
import os


base = "https://api.themoviedb.org/3/"
#url = 'movie/popular'  #API method 
url = 'movie/379686'  #API method 
query_term = 'titanic'

api_key = os.environ["TMDB_API_KEY"]

endpoint = base + url #combining it together # print(endpoint)
res = re.get(endpoint,  #use endpoint and all the parameters we need in a dictionary
                     # params={'query': query_term, 'api_key': api_key})
                        params={ 'api_key': api_key})



res_j = res.json()


#print(res.status_code)

#print(len(res_j))
import pprint

#pprint.pprint(res_j)


c_ov=(len(res_j['overview']))

print('Favorite Movie:', res_j['original_title'] , '\n'
      'Release Date:'  , res_j['release_date']   , '\n'
      'runtime:'       , res_j['runtime']   , '\n'
      'revenue:'       , res_j['revenue']   , '\n'
      'length of the overview:'       , str(c_ov)   , '\n'
      'number of votes'       , res_j['vote_count']   , '\n'
      'voting average:'       , res_j['vote_average']   
      )

exit()
