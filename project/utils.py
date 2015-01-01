# -*- coding: utf-8 -*-
"""
A range of utilities to be used project wide.
"""

import requests


## =============================================================================
## PyVideo connection


def fetch_pyvideo_link_json(url, pk):
    """ Sanity check on pyvideos link fetching.
    """
    if any([pk<99999, not str(pk)[5:]]):
        request =  requests.get('{0}{1}'.format(url, pk))
        if request.ok:
            return request.json()
        else:
            raise Exception("PyVideo API end point doesn't exist.")
    else:
        raise Exception("Inputed pk looks suspicious.")
