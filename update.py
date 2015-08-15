import json
import urllib.parse
import urllib.request
import re
import logging as log
import os.path

def error(msg):
    log.error(msg)

    
def get_icons(img_type, id_list, version, overwrite=False):
    '''
Download all icons.

Parameters
-------------
img_type : str
    What type of icon should we fetch (ex. champion or item).
id_list : list[str]
    List of all the icon ids to fetch.
version : str
    Version to download in format 5.15.1
overwrite : bool
    If we want to overwrite icons if 
    it already exists.
    '''
    log.debug("Fetching " + img_type + " icons, using version " + version)
    
    for icon_id in id_list:
        url = "http://ddragon.leagueoflegends.com/cdn/" + version + \
              "/img/" + img_type + "/" + icon_id+".png"
        
        try:
            with urllib.request.urlopen(url) as response:
                # Check if it already exists and if we're to overwrite existing files.
                if (os.path.exists("icons/" + img_type + "/" + icon_id + ".png") and not overwrite):
                    log.debug("Skipping file - icons/" + img_type + "/" + icon_id + ".png")
                else:
                    log.debug("Writing icon id " + icon_id)
                    with open("icons/" + img_type + "/" + icon_id + ".png",'wb') as image_file:
                        image_file.write(response.read())
                        
        except urllib.error.HTTPError:
            error("Error when downloading icon id " + icon_id)

    log.debug("Done fetching all icons")

    
def get_json(json_type, url, region):  
    '''
Fetch json file.

Parameters
-------------
json_type : str
    What type of json we want to fetch (ex. champion or item).
url : str
    URL to fetch json from.
region : str
    Region code for which region we
    want to fetch from.

Returns
-------------
html : str
    This is a json file with all
    the items for the given region.
    '''
    icon_id_list = []
    log.debug("Fetching " + json_type + " for " + region)
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("UTF-8")
    except urllib.error.HTTPError:
        error("HTTPError when trying to access " + url)
        return None
        
    # Temporary way of getting item icons
    # will be replaced later when db is up and running.
    if ("na" in region):
        html_json = json.loads( html )

        for icon_id in html_json["data"]:
            icon_id_list.append(icon_id)

        get_icons(json_type, icon_id_list, "5.15.1")
                             
    log.debug("Succesfully fetched items for " + region)
    
    return html

    
def check_json_version(json_type, net_json_string, region):
    '''
Compare local version of file to the one on the net.

Parameters
-------------
net_json_string : str
    String version of JSON file we
    fetched via the API.
region : str
    Region code for the JSON file.

Returns
-------------
is_new_version : bool
    True if there is a newer version or
    no local version. False else.
    '''
    log.debug("Checking file versions for " + region)
    
    # If we can't find the file, we want to save it.
    try:
        local_json_file = open("json/" + json_type + "/" + region,'r')
    except FileNotFoundError:
        return True
    
    local_json_version = json.load(local_json_file)
    net_json_version = json.loads(net_json_string)

    log.debug("Net version: " + net_json_version["version"] + \
              "\tLocal version: " + local_json_version["version"])

    if (local_json_version["version"] == net_json_version["version"]):
        is_new_version = False
    else:
        is_new_version = True

    return is_new_version


def get_all_json(url_list, region_list):
    '''
Fetch all the json.

Parameters
-------------
url_list : list[str]
    List of all the different types we want
    and url that comes we fetch from.
region_list : list[str]
    List of all the different regions we fetch.
    '''
    log.debug("Beginning fetching for all json files for all regions")
        
    for json_type in url_list:
        for region in region_list:
            
            url = url_list[json_type]
            json_string = get_json(json_type, url, region)
            
            if (json_string is None):
                log.error("Error occured when trying to fetch items for " + region)
                continue
            else:
                if (check_json_version( json_type, json_string, region )):
                    with open("json/" + json_type + "/" + region, 'w') as json_file:
                        json_file.write( json_string )
                else:
                    log.debug(region + " skipped because it was up to date.")
                    
    log.debug("Fetched all items as json files for all regions")

    
def update_all(api_key, current_version, loglvl):
    log.basicConfig(format="%(levelname)s: %(message)s", level=loglvl)
    
    region_list = ["br","eune","euw","kr","lan","las","na","oce","ru","tr","pbe"]
    #region_list = ["na"]
    url_list = {"item":"https://global.api.pvp.net/api/lol/static-data/eune/v1.2/item?itemListData=all&api_key="+api_key,
                "champion":"https://global.api.pvp.net/api/lol/static-data/eune/v1.2/champion?champData=all&api_key="+api_key}
    
    get_all_json(url_list, region_list)
