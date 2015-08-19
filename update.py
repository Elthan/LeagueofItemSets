import json
import urllib.parse
import urllib.request
import re
import logging as log
import os.path
from convert import create_db_json_items
from convert import create_db_json_champ
from database.models import Version
from database.models import Champion
from database.models import Item


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
        log.warning("HTTPError " + err + "when checking version for " + \
            region + ". Version set to 5.15.1")
        net_version = "5.15.1"

    net_version = json.loads(net_version)[0]

    try:
        # Read local version in DB
        query = Version.objects.get(Region=region)
    except Version.DoesNotExist:
        log.warning("Could not find " + region + " in DB when checking for region")
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

    
def get_icons(img_type):
    '''
Download all icons using ids in DB.

Parameters
-------------
img_type : str
    What type of icon should we fetch (ex. champion or item).
    '''

    if (img_type == "item"):
        query = Item.objects.all()
    elif (img_type == "champion"):
        query = Champion.objects.all()
    else:
        error("Image type not supported for " + img_type + ". Unable to fetch icons.")
        return
        
    log.debug("Fetching " + img_type + " icons.")
    
    for icon_id in query:
        if (img_type == "item"):
            icon_id = str(icon_id.pk)
        elif (img_type == "champion"):
            icon_id = icon_id.Name
        
        url = "http://ddragon.leagueoflegends.com/cdn/" + current_version + \
              "/img/" + img_type + "/" + icon_id+".png"

        try:
            with urllib.request.urlopen(url) as response:
                path = "icons/" + img_type + "/" + icon_id + ".png"

                with open(path,'wb') as image_file:
                    image_file.write(response.read())
                        
        except urllib.error.HTTPError:
            error("Error when downloading icon id " + icon_id + "\nUsing url " + url)

    log.info("Done fetching all icons of type " + img_type)

    
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
    log.debug("Fetching " + json_type + " for " + region)
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("UTF-8")
    except urllib.error.HTTPError:
        error("HTTPError when trying to access " + url)
        return None
            
    log.debug("Succesfully fetched items for " + region)
    
    return html


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
            with open("json/" + json_type + "/" + region + ".json", 'w') as json_file:
                json_file.write(json_string)
                
    log.info("Fetched all items as json files for region " + region)

    
def update_all(api_key, cur_ver, loglvl, region, skip_icons, skip_json, skip_convert, skip_write_db):
    '''
Master method for updating everything; icons, JSONs and DB.

Parameters
-------------
api_key : str
    Key to make API calls to Riot servers.
cur_ver : str
    Current version in the format 5.15.1
loglvl : str
    What level we should log at.
region : str
    What region we should update data for. This doesn't matter
    for icons.
skip_icons : bool
    If we should skip downloading icons.
skip_json : bool
    If we should skip downloading JSON files.
skip_convert : bool
    If we should skip converting JSON files to DB friendly JSON files.
skip_write_db : bool
    If we should skip writing JSON files to database.
    '''
    log.basicConfig(format="%(levelname)s: %(message)s", level=loglvl)
     
    url_list = {
        "item":"https://global.api.pvp.net/api/lol/static-data/eune/v1.2/item?itemListData=all&api_key=" + api_key,
        "champion":"https://global.api.pvp.net/api/lol/static-data/eune/v1.2/champion?champData=all&api_key=" + api_key 
    }

    global current_version
    current_version = cur_ver.strip()
    
    if (skip_json):
        log.info("Skipping all json files.")
    else:
        get_all_json(url_list, region)

    if (skip_convert):
        log.info("Skipping converting JSON files.")
    else:
        create_db_json_items(region, log)
        create_db_json_champ(region, log)

    if (skip_write_db):
        log.info("Skipping writing JSONs to DB.")
    else:
        # Get the command and setup django so we can execute it
        from django.core.management import call_command
        import django
        django.setup()

        log.debug("Creating backup of DB.")
        call_command("dumpdata", "database", "--output=db_backup.json")

        json_types = ["item", "item_stats", "champion", "champ_stats"]
        
        for json_type in json_types:
            path = "json/" + json_type + "/" + region + "/"
            
            for path, subdirs, files in os.walk(path):
                for name in files:
                    call_command("loaddata", path + name, '--ignorenonexistent', verbosity=0)
             
            log.info("All " + json_type + " JSON files imported to the DB.")
            
    if (skip_icons):
        log.info("Skipping all icons.")
    else:
        for icon_type,url in url_list.items():
            get_icons(icon_type)
