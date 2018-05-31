import json
import random
import string
import sys


def get_filtered_keys(key_list, payload):
    """
    Filter the payload for the given keylist and return the filtered dict
    :param key_list: comma seperated keys in string format
    :param payload: dict payload which needs to be filtered
    :return: dict with key, value pair based on the keylist





    """

    ret_dict = dict()

    key_list = str(key_list).split(",")

    for key in key_list:
        value = payload.get(key)
        if not value:
            raise \
                KeyError("Key: {} not present in payload: {} for "
                         "keylist: {}"
                         .format(key, payload, key_list))
        ret_dict[key] = value
    return ret_dict


def get_filtered_keys_from_map(key_map, payload):
    """
    Filter the payload for the given keylist and return the filtered dict
    :param key_list: a json old_key:new_key map in string format
    :param payload: dict payload which needs to be filtered
    :return: dict with new_key, value pair based on the keylist
    """

    ret_dict = dict()
    key_map = json.loads(key_map)

    for old_key, new_key in key_map:
        value = payload.get(old_key)
        if not value:
            raise KeyError("Key: {} not present in payload: {} for key map: "
                           "{}"
                           .format(old_key, payload, key_map))
        ret_dict[new_key] = value
    return ret_dict


def update_import_paths(import_paths):
    """
    update the import paths in the system
    :param import_paths:
    :return:
    """
    if import_paths:
        sys.path = import_paths.split(':') + sys.path


def generate_unique_id(size=5):
    return ''.join(random.choice(string.digits) for _ in range(size))
