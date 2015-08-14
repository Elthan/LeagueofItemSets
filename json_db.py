import json
import urllib.parse
import urllib.request
import re

def error(msg, log):
    log.error(msg)
    exit(-1)

def get_icon(version, icon_id):
    '''
Download icon file and save it in icons/
    '''
    log.debug("Fetching icon with id: "+icon_id+", version: "+version)
    
    url = "http://ddragon.leagueoflegends.com/cdn/"+version+"/img/item/"+icon_id
    
    icon_file, headers = urllib.request.urlretrieve(url)
    icon_file_content = open(icon_file)
    icon_file_save = open("icons/"+ic_id,'wb')
    icon_file_save.write(icon_file_content)
    
    log.debug("Successfully saved icon image")
    
def get_items(region, api_key, log):  
    '''
Fetch file from given region.
    '''

    log.debug("Fetching items for "+region)
    
    url = "https://global.api.pvp.net/api/lol/static-data/"+region+ \
          "/v1.2/item?itemListData=all&api_key=" + api_key
    html = ""
    
    with urllib.request.urlopen(url) as response:
        if (response.status != 200):
            error(response.status)
        html = response.read()
        
    log.debug("Succesfully fetched items for "+region)

    return html.decode("UTF-8")


def get_all_items(region_list, api_key, log):
    '''
Fetch all the items! (as json files)
    '''
    
    log.info("Beginning download for all items as json files for all regions")

    for region in region_list:   
        net_items_string = get_items(region, api_key, log)

        if (check_items_version(net_items_string, region, log)):
            net_items_file = open("items_json/"+region,mode='w')
            net_items_file.write(net_items_string)
            net_items_file.close()
        else:
            log.debug(region+" skipped because it was up to date.")
       
    log.info("Downloaded all items as json files for all regions")

    
def check_items_version(net_items_string, region, log):
    '''
Compare local version of file to the one on the net.
    '''
    log.info("Checking file versions for "+region)
    
    try:
        local_items_file = open("items_json/"+region,'r')
    except FileNotFoundError:
        return True
    
    local_items_json = json.load(local_items_file)

    log.debug("Local version: "+local_items_json["version"])

    net_items_json = json.loads(net_items_string)

    log.debug("Net version: "+net_items_json["version"])

    if (local_items_json["version"] == net_items_json["version"]):
        return False
    else:
        return True
