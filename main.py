#!/usr/bin/env python3

import update
import logging as log
import re
import urllib.request
import json

#######################################
# 
#   League of Item Sets
#
#   Version: 0.1
#
#   By: Jonas Sandbekk & Ole Harbosen
# 
#   In collaberation with Riot Games
#
#   For the Riot API Challenge 2.0
#
#######################################

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
            net_version = response.read().decode("UTF-8")
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


if __name__ == "__main__":
  
    # Set level of logging to be done
    log.basicConfig(format="%(levelname)s: %(message)s",level="DEBUG")

    print("League of Item Sets v0.1")
    
    # Get the api_key, which is hidden for git purposes
    try:
        with open("settings") as settings_file:
            settings_string = settings_file.read()
            api_key = re.search(r'API_KEY:\s*([?\w\d\-]+)\s', settings_string)

            if (api_key is None):
                log.error("""Could not locate api_key inside settings file.
                Please input an api_key in the settings file in the format: 
                API_KEY: <API_KEY>""")
            else:
                api_key = api_key.group(1)

            # This is temporary. Will be exchanged once we have a db with a table
            # which contains all versions for all regions
            current_version = re.search(r'CURRENT_VERSION: ([?\d\.]+\s)', settings_string)

            if (current_version is None):
                log.error("""Could not locate the current version inside the settings file.
                Please input the current version inside the settings file in format:
                CURRENT_VERSION: <VERSION>""")
            else:
                current_version = current_version.group(1)

            # Temporary just use eune
            if (check_version( "eune", api_key, current_version )):
                log.debug("We are up to date!")
            else:
                # Update all the json file from all the different regions
                update.update_all(api_key, current_version, "DEBUG")
                
    except FileNotFoundError:
        log.error("Settings file not found. Please create a settings file.")
