#!/usr/bin/env python3

import update
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
  
    # Set level of logging to be done
    log.basicConfig(format="%(levelname)s: %(message)s",level="DEBUG")

    print("League of Item Sets v0.1")
    
    # Get the api_key, which is hidden for git purposes
    with open("settings") as api_key_file:
        api_key_string = api_key_file.read()
        api_key = re.search(r'API_KEY:\s*([?\w\d\-]+)\s', api_key_string).group(1)

    # Update all the json file from all the different regions
    update.get_all_items(api_key, log)
