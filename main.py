#!/usr/bin/env python3

import json_db
import logging as log
import re

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


if __name__ == "__main__":
    region_list = ["br","eune","euw","kr","lan","las","na","oce","ru","tr","pbe"]
    
    # Set level of logging to be done
    log.basicConfig(format="%(levelname)s: %(message)s",level="DEBUG")

    print("League of Item Sets v0.1")
    
    # Get the api_key, which is hidden for git purposes
    with open("settings") as api_key_file:
        api_key_string = api_key_file.read()
        api_key = re.findall(r'API_KEY:\s*([?\d-]+)\s', api_key_string).group(1)

    # Get all the json files from all the different regions
    json_db.get_all_items(region_list, api_key, log)
