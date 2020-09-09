# -*- coding: utf-8 -*-

"""I/O

Provides all necessary I/O Operations and file utils

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi@ibm.com>
"""

import os
import csv
import json
from typing import List

from coffee.utils.logger import Logger


def jsonToDict(path: str) -> dict:
    """loads JSON from a file and converts to a dict

    Parameters
    ----------
    path : str
        path to json file 

    Returns
    -------
    dict
        json object as a dict
    """
    logger = Logger().logger
    try:
        json_file = open(path, "r")
        json_data = json_file.read()
        json_file.close()

        return json.loads(json_data)
    except ValueError as e:
        Logger().error(1, f"Error: cannot load JSON at path: {path}. Invalid json: {e}")
    except Exception as e:
        logger.debug(e)
        Logger().error(
            1, f"Error: Cannot load json data from path: {path}",
        )


def saveJSON(path: str, data: dict):
    """Save a python dict to a json file

    Parameters
    ----------
    path : str
        path to save json file 
    data : [type]
        python dict
    """
    logger = Logger().logger
    try:
        file = open(path, "w+")
        file.write(json.dumps(data, indent=4))
        file.close()
    except Exception as e:
        logger.debug(e)
        Logger().error(
            1, f"Error: Cannot save json to path: {path}",
        )
