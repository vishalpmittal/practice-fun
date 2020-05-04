import os
import json
from datetime import datetime
from typing import List


def archive_file(curr_file_path, archive_dir):
    if not os.path.exists(curr_file_path):
        return
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    archive_file = os.path.join(archive_dir, os.path.basename(curr_file_path))
    os.rename(curr_file_path, archive_file)


def write_lines_to_file(dir_path: str, file_name: str, data_lines: List[str]):
    if not dir_path or not file_name or not data_lines:
        return

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    write_file = os.path.join(dir_path, file_name)

    with open(write_file, 'w') as fp:
        for line in data_lines:
            fp.write(data_lines)


def read_data(file_path):
    if not os.path.isfile(file_path):
        return None
    try:
        with open(file_path, 'r') as fp:
            return fp.read()
    except IOError:
        return None


def get_file_mod_ts_str(full_path):
    return (datetime.fromtimestamp(os.path.getmtime(full_path))).strftime(
        '%Y%m%dT%H%M%S'
    )
