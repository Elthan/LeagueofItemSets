#!/usr/bin/env python3

import logging as log
import re
import argparse
import os

# Required that DJANGO_SETTINGS_MODULE is not set already.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LeagueofItemSets.settings")

import update
import convert

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

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--force', default=False, action="store_true",
                        help="Force update even if it's up to date. (default: %(default)s)")
    parser.add_argument('-v', '--verbose', action="store_const", const="DEBUG",
                        default="INFO", help="Set output level to DEBUG.")
    parser.add_argument('-i', '--skipicons', action="store_true", default=False,
                        help="Skip downloading icons. (default: %(default)s)")
    parser.add_argument('-j', '--skipjson', action="store_true", default=False,
                        help="Skip downloading JSON files. (default: %(default)s)")
    parser.add_argument('-c', '--skipconvert', action="store_true", default=False,
                        help="Skip converting JSON to DB friendly JSON. (default: %(default)s)")
    parser.add_argument('-d', '--database', action="store_true", default=False,
                        help="Skip writing all JSON files to the database. (default: %(default)s)")
    
    args = parser.parse_args()
    loglvl = args.verbose
    skip_icons = args.skipicons
    skip_json = args.skipjson
    skip_convert = args.skipconvert
    skip_write_db = args.database
    force_update = args.force
    
    # Set level of logging to be done
    log.basicConfig(format="%(levelname)s: %(message)s",level=loglvl)
    
    
    # Temporary use only eune
    #region_list = ["br","eune","euw","kr","lan","las","na","oce","ru","tr","pbe"]
    region_list = ["eune"]
    
    log.info("League of Item Sets v0.3")

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
                    update.update_all(api_key, current_version, "DEBUG", region,
                                      skip_icons, skip_json, skip_convert, skip_write_db)
                else:
                    log.info("We are up to date for " + region + "!")
                
    except OSError as oserr:
        print(oserr)
        log.error("Settings file not found. Please create a settings file.")
