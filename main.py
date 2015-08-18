#!/usr/bin/env python3

import update
import logging as log
import re

#######################################
#
#   League of Item Sets
#
#   Version: 0.3
#
#   By: Jonas Sandbekk & Ole Harbosen
#
#   In collaberation with Riot Games
#
#   For the Riot API Challenge 2.0
#
#######################################


if __name__ == "__main__":
    # Set level of logging to be done
    log.basicConfig(format="%(levelname)s: %(message)s",level="DEBUG")

    force_update = False

    # Temporary use only eune
    #region_list = ["br","eune","euw","kr","lan","las","na","oce","ru","tr","pbe"]
    region_list = ["eune"]
    
    print("League of Item Sets v0.3")

    # Get the api_key, which is hidden.
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

            for region in region_list:
                is_new_version, current_version = update.check_version(region, api_key, log)
                
                if (is_new_version or force_update):
                    # Update all the json file from all the different regions.
                    update.update_all(api_key, current_version, "DEBUG", region)
                else:
                    log.debug("We are up to date for " + region + "!")

    except OSError as oserr:
        print(oserr)
        log.error("Settings file not found. Please create a settings file.")
