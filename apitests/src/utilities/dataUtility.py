import json
import os


def request_json_file(file_name):
    cur_file_dir = os.path.dirname(os.path.realpath(__file__))
    payload_template = os.path.join(cur_file_dir, '..', 'testData', file_name)
    with open(payload_template) as f:
        payload = json.load(f)

    return payload
