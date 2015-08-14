#!/usr/bin/env python3

import json_db
import logging as log

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
    with open("api_key") as api_key_file:
        api_key = api_key_file.read()

    # Get all the json file from all the different regions
    json_db.get_all_items(region_list, api_key, log)
