import json
import urllib.parse
import urllib.request

def error(msg, log):
    log.error(msg)
    exit(-1)


def get_items(region, api_key, log):  
    '''
Fetch file from given region.
    '''

    log.debug("Fetching items for "+region)
    
    url = "https://global.api.pvp.net/api/lol/static-data/"+region+ \
          "/v1.2/item?itemListData=all&api_key=" + api_key

    response = urllib.request.urlopen(url)

    if (response.status != 200):
        error(response.status)
        
    log.debug("Succesfully fetched items for "+region)

    return response.read().decode("UTF-8")


def get_all_items(region_list, api_key, log):
    '''
Fetch all the items! (as json files)
    '''
    
    log.info("Beginning download for all items as json files for all regions")

    for region in region_list:   
        new_items_json = get_items(region, api_key, log)
        
        new_items_file = open("./items_json/"+region,mode='w')
        new_items_file.write(new_items_json)
        
        new_items_file.close()
        
    log.info("Downloaded all items as json files for all regions")

    
def check_items_version():
    '''
Check current version of files versus whats online.
    '''
    pass
    
