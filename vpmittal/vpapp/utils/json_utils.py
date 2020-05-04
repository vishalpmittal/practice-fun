import os
import json
from collections import OrderedDict


def fd_helper(fl_dict, prev_value, prev_key=''):
    """
    Recursive helper method for flatten_dict
    """
    if not isinstance(prev_value, dict):
        fl_dict[prev_key] = prev_value
    else:
        for sub_key, sub_val in prev_value.iteritems():
            if prev_key:
                new_key = '{}_{}'.format(prev_key, sub_key)
            else:
                new_key = '{}{}'.format(prev_key, sub_key)
            fd_helper(fl_dict, sub_val, new_key)


def flatten_dict(dict_of_dict):
    """
    :param dict_of_dict: can be any level of nested dictionary
    :return: returns a dictionary of 1 level with appended keys and respective values
    """
    if not dict_of_dict or not isinstance(
            dict_of_dict, dict) or not dict_of_dict:
        return dict_of_dict

    fl_dict = OrderedDict()
    fd_helper(fl_dict, dict_of_dict)
    return fl_dict


def read_json(file_path):
    if not os.path.isfile(file_path) or file_path.split('.')[-1] != 'json':
        return None
    try:
        with open(file_path, 'r') as fp:
            return json.load(fp)
    except IOError:
        return None


def write_json_to_file(dir_path, file_name, json_data):
    if not dir_path or not file_name or not json_data:
        return

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    write_file = os.path.join(dir_path, file_name)

    with open(write_file, 'w') as fp:
        json.dump(json_data, fp, sort_keys=True, indent=2)
