import django.db
from database.models import Version

def check_version(region, api_key, local_version):
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
        error("HTTPError when checking version for " + region)
        return False, current_version

    net_version = json.loads(net_version)[0]

    try:
        query = Version.objects.all()
    except DoesNotExist:
        pass
    except MultipleObjectsReturned:
        pass


    if (local_version == net_version):
        current_version = local_version
        is_new_version = False
    else:
        current_version = net_version
        is_new_version = True

    return is_new_version, current_version
