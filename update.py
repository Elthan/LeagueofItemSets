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
    
    with open("icons/"+icon_id,'wb') as icon_file:
        icon_file.write( urllib.request.urlopen(url).read() )
    
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
        html = response.read().decode("UTF-8")
    
    if ("na" in region):
        html_json = json.loads( html )
        
        for image_id in html_json["data"]:
            url_images = "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/"+ \
                image_id+".png"
            with urllib.request.urlopen(url) as response:
                if (response.status != 200):
                    error("Error when downloading image id "+image_id+": "+\
                              response.status)
                with open("icons/"+image_id,'w') as image_file:
                    image_file = write(html)
                
    log.debug("Succesfully fetched items for "+region)

    return html


def get_all_items(api_key, log):
    '''
Fetch all the items! (as json files)
    '''
    region_list = ["br","eune","euw","kr","lan","las","na","oce","ru","tr","pbe"]
    
    log.debug("Beginning download for all items as json files for all regions")

    for region in region_list:   
        items_string = get_items(region, api_key, log)
        
        if (check_items_version(items_string, region, log)):
            with open("json/items/"+region,'w') as items_file:
                items_file.write(net_items_string)
        else:
            log.debug(region+" skipped because it was up to date.")
       
    log.debug("Downloaded all items as json files for all regions")
    
def check_items_version(net_items_string, region, log):
    '''
Compare local version of file to the one on the net.
    '''
    log.debug("Checking file versions for "+region)
    
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
