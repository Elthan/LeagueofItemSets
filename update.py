import json
import urllib.parse
import urllib.request
import re
import logging as log
import os.path

def error(msg):
    log.error(msg)

    
def check_version(region, api_key, local_version):
    '''
Check current version of the region.

Parameters
-------------
region : str
    Region to be examined
api_key : str
    Api_key to use in request
local_version : str
    Local version for region in format 5.15.1

Returns
-------------
new_version : bool
    True for new version, False else
current_version : str
    The current version for the region
    in the format 5.15.1
    '''
    log.debug("Checking version for "+region)
    
    url = "https://global.api.pvp.net/api/lol/static-data/" + region + \
          "/v1.2/versions?api_key=" + api_key
    
    try:
        with urllib.request.urlopen(url) as response:
            net_version = response.read()
    except urllib.error.HTTPError:
        error("HTTPError when version checking for " + region)
        return False, current_version

    net_version = json.loads(net_version)[0]
    
    if (local_version == net_version):
        current_version = local_version
        is_new_version = False
    else:
        current_version = net_version
        is_new_version = True

    return is_new_version, current_version


def get_icons(img_type, id_list, version, overwrite=False):
    '''
Download all icons.

Parameters
-------------
img_type : str
    What type of icon should we fetch (ex. champion or item)
id_list : list[str]
    List of all the icon ids to fetch
version : str
    Version to download in format 5.15.1
overwrite : bool
    If we want to overwrite icons if 
    it already exists
    '''
    log.debug("Fetching " + img_type + " icons, using version " + version)
    
    for icon_id in id_list:
        url = "http://ddragon.leagueoflegends.com/cdn/" + version + \
              "/img/" + img_type + "/" + icon_id+".png"
        
        try:
            with urllib.request.urlopen(url) as response:
                # Check if it already exists and if we're to overwrite existing files
                if (os.path.exists("icons/" + img_type + "/" + icon_id + ".png") and not overwrite):
                    log.debug("Skipping file - icons/" + img_type + "/" + icon_id + ".png")
                else:
                    log.debug("Writing icon id " + icon_id)
                    with open("icons/" + img_type + "/" + icon_id + ".png",'wb') as image_file:
                        image_file.write(response.read())
                        
        except urllib.error.HTTPError:
            error("Error when downloading icon id " + icon_id)

    log.debug("Done fetching all icons")

    
def get_items(region, api_key):  
    '''
Fetch json file with items.

Parameters
-------------
region : str
    Region code for which region we
    want to download from.
api_key : str
    Api key to use for request

Returns
-------------
html : str
    This is a json file with all
    the items for the given region.
    '''
    items_id_list = []
    log.debug("Fetching items for " + region)
    
    url = "https://global.api.pvp.net/api/lol/static-data/" + region + \
          "/v1.2/item?itemListData=all&api_key=" + api_key

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("UTF-8")
    except urllib.error.HTTPError:
        error("HTTPError when trying to access " + url)
        return None
        
    # Temporary way of getting item icons
    # will be replaced later when db is up and running
    if ("na" in region):
        html_json = json.loads( html )

        for image_id in html_json["data"]:
            items_id_list.append(image_id)

        get_icons("item", items_id_list, "5.15.1")
                             
    log.debug("Succesfully fetched items for " + region)
    
    return html

    
def check_items_version(net_items_string, region):
    '''
Compare local version of file to the one on the net.

Parameters
-------------
net_items_string : str
    String version of JSON file we
    fetched via the API.
region : str
    Region code for the JSON file.

Returns
-------------
is_new_version : bool
    True if there is a newer version or
    no local version. False else
    '''
    log.debug("Checking file versions for " + region)
    
    # If we can't find the file, we want to save it
    try:
        local_items_file = open("items_json/" + region,'r')
    except FileNotFoundError:
        return True
    
    local_items_json = json.load(local_items_file)

    log.debug("Local version: " + local_items_json["version"])

    net_items_json = json.loads(net_items_string)

    log.debug("Net version: " + net_items_json["version"])

    if (local_items_json["version"] == net_items_json["version"]):
        is_new_version = False
    else:
        is_new_version = True

    return is_new_version


def get_all_items(api_key, loglvl):
    '''
Fetch all the items! (as json files)

Parameters
-------------
api_key : str
    Api key to use for requests
loglvl : str
    At which level we should print logging
    '''
    #region_list = ["br","eune","euw","kr","lan","las","na","oce","ru","tr","pbe"]
    region_list = ["na"]
    
    log.basicConfig(format="%(levelname)s: %(message)s", level=loglvl)
    
    log.debug("Beginning fetching for all items as json files for all regions")
        
    for region in region_list:   
        items_string = get_items( region, api_key )

        if (items_string is None):
            log.error("Error occured when trying to fetch items for " + region)
            continue
        
        if (check_items_version( items_string, region )):
            with open("json/items/" + region, 'w') as items_file:
                items_file.write( items_string )
        else:
            log.debug(region + " skipped because it was up to date.")
       
    log.debug("Fetched all items as json files for all regions")
