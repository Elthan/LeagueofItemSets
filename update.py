import json
import urllib.parse
import urllib.request
import re
import logging as log
import os.path
from convert import create_db_json_items
from convert import create_db_json_champ

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LeagueofItemSets.settings")

from database.models import Version


def error(msg):
    log.error(msg)
   

def check_version(region, api_key, log):
    '''
Check current version of the region.

Parameters
-------------
region : str
    Region to be examined.
api_key : str
    Api_key to use in request.
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
            net_version = response.read().decode("UTF-8")
    except urllib.error.HTTPError as err:
        error("HTTPError " + err + "when checking version for " + \
            region + ". Version set to 5.15.1")
        net_version = "5.15.1"

    net_version = json.loads(net_version)[0]

    try:
        # Read local version in DB
        query = Version.objects.get(Region=region)
    except Version.DoesNotExist:
        log.debug("Could not find " + region + " in DB when checking for region")
        log.debug("Creating " + region + " in DB with version " + net_version)
        new_entry = Version(Region=region, Version=net_version)
        new_entry.save()
        return True, net_version
    except Version.MultipleObjectsReturned:
        error("Multiple objects returned when checking for region version")
        return True, net_version

    local_version = query.Version

    if (local_version == net_version):
        current_version = local_version
        is_new_version = False
    else:
        current_version = net_version
        is_new_version = True

    return is_new_version, current_version

    
def get_icons(img_type, id_list):
    '''
Download all icons.

Parameters
-------------
img_type : str
    What type of icon should we fetch (ex. champion or item).
id_list : list[str]
    List of all the icon ids to fetch.
    '''
    if (skip_icons):
        log.debug("Skipping all icons")
        return
    
    log.debug("Fetching " + img_type + " icons, using version " + current_version)
    
    for icon_id in id_list:
        url = "http://ddragon.leagueoflegends.com/cdn/" + current_version + \
              "/img/" + img_type + "/" + icon_id+".png"
        
        try:
            with urllib.request.urlopen(url) as response:
                path = "icons/" + img_type + "/" + icon_id + ".png"
                
                # Check if it already exists and if we're to overwrite existing files.
                if (os.path.exists(path) and not overwrite):
                    log.debug("Skipping icon " + img_type + "/" + icon_id)
                else:
                    log.debug("Writing icon id " + icon_id)
                    with open(path,'wb') as image_file:
                        image_file.write(response.read())
                        
        except urllib.error.HTTPError:
            error("Error when downloading icon id " + icon_id + "\nUsing url " + url)

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
    if ("eune" in region):
        html_json = json.loads( html )

        for icon_id in html_json["data"]:
            icon_id_list.append(icon_id)

        get_icons(json_type, icon_id_list)
                             
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
        local_json_file = open("json/" + json_type + "/" + region + ".json",'r')
    except OSError:
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


def get_all_json(url_list, region):
    '''
Fetch all the json.

Parameters
-------------
url_list : list[str]
    List of all the different types we want
    and url that comes we fetch from.
region : str
    Region we should fetch for.
    '''
    log.debug("Beginning fetching for all json files for region " + region)
        
    for json_type in url_list:
        url = url_list[json_type]
        json_string = get_json(json_type, url, region)
        
        if (json_string is None):
            error("Error occured when trying to fetch items for " + region)
            continue
        else:
            if (check_json_version( json_type, json_string, region ) and overwrite
                or not skip_json):
                with open("json/" + json_type + "/" + region + ".json", 'w') as json_file:
                    json_file.write(json_string)
            else:
                log.debug(region + " skipped because it was up to date.")
                
    log.debug("Fetched all items as json files for region " + region)

    
def update_all(api_key, cur_ver, loglvl, region, ow=False, skip_ic=False, skip_js=False):
    log.basicConfig(format="%(levelname)s: %(message)s", level=loglvl)
    
 
    url_list = {"item":"https://global.api.pvp.net/api/lol/static-data/eune/v1.2/item?itemListData=all&api_key="+api_key,
                "champion":"https://global.api.pvp.net/api/lol/static-data/eune/v1.2/champion?champData=all&api_key="+api_key}

    global current_version
    current_version = cur_ver.strip()
    global overwrite
    overwrite = ow
    global skip_icons
    skip_icons = skip_ic
    global skip_json
    skip_json = skip_js
    
    get_all_json(url_list, region)
    
    log.debug("Converting json files to django friendly json files.")
    create_db_json_items(region, log, overwrite=overwrite)
    create_db_json_champ(region, log, overwrite=overwrite)
