import json
import os
import logging

logger = logging.getLogger("foodiz")


def read_json(file_path):
    """
        utility method to read a json file
        returns json object
    """
    if not os.path.isfile(file_path) or file_path.split(".")[-1] != "json":
        return None
    try:
        with open(file_path, "r") as fp:
            logger.info("Successfully read the json file: {}".format(file_path))
            return json.load(fp)
    except IOError:
        logger.error("Unable to read the json file: {}".format(file_path))
        return None
