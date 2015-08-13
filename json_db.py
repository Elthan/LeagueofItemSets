import json
import urllib.parse
import urllib.request

def error(msg):
    log.error(msg)
    exit(-1)


def get_items(region, api_key, log):  
    log.debug("Fetching items for "+region)
    
    url = "https://global.api.pvp.net/api/lol/static-data/"+region+ \
          "/v1.2/item?itemListData=all&api_key=" + api_key

    response = urllib.request.urlopen(url)

    if (response.status != 200):
        error(response.status)
        
    log.debug("Succesfully fetched items for "+region)

    return response.read().decode("UTF-8")
