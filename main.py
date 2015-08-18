#!/usr/bin/env python3

import update
import logging as log
import re
import version_check
import os

#######################################
#
#   League of Item Sets
#
#   Version: 0.2
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

    # This might not work, may have to set the env var manually.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LeagueofItemSets.settings")

    print("League of Item Sets v0.2")

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

            is_new_version, current_version = version_check.check_version("eune", api_key, log)
            # Temporary just use eune
            if (is_new_version):
                # Update all the json file from all the different regions.
                update.update_all(api_key, current_version, "DEBUG")
            else:
                log.debug("We are up to date!")

    except OSError as oserr:
        print(oserr)
        log.error("Settings file not found. Please create a settings file.")
