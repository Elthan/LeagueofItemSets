import urllib.request
import json
from database.models import Version


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
    except urllib.error.HTTPError:
        error("HTTPError when checking version for " + region + \
                ". Version set to 5.15.1")
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
        log.error("Multiple objects returned when checking for region version")
        return True, net_version

    local_version = query.Version

    if (local_version == net_version):
        current_version = local_version
        is_new_version = False
    else:
        current_version = net_version
        is_new_version = True

    return is_new_version, current_version
