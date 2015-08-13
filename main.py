#!/usr/bin/env python3

import json_db
import logging as log

#######################################
# 
#   League of Item Sets
#
#   Version: 0.0
#
#   By: Jonas Sandbekk & Ole Harbosen
# 
#   In collaberation with Riot Games
#
#   For the Riot API Challenge 2.0
#
#######################################


def get_all_items(region_list):
    log.info("Beginning download for all items as json files for all regions")
    for region in region_list:   
        new_items_json = json_db.get_items(region,api_key,log)
        
        new_items_file = open("./items_json/"+region,mode='w')
        new_items_file.write(new_items_json)
        
        new_items_file.close()
        
    log.info("Downloaded all items as json files for all regions")

def check_items_version():
    pass
    

if __name__ == "__main__":
    region_list = ["br","eune","euw","kr","lan","las","na","oce","ru","tr","pbe"]
    
    # Set level of logging to be done
    log.basicConfig(format="%(levelname)s: %(message)s",level="DEBUG")

    print("League of Item Sets v0.1")
    
    # Get the api_key, which is hidden for git purposes
    api_key_file = open("api_key")
    api_key = api_key_file.read()
    api_key_file.close()

    if (False):
        get_all_items(region_list)
