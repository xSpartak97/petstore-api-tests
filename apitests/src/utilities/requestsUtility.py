from apitests.src.configs.host_config import API_HOSTS
import requests
import os
import json
import logging as logger


class RequestsUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'main')
        self.base_url = API_HOSTS[self.env]

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            f"Bad Status code." \
            f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
            f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None, params=None, expected_status_code=200):
        if not headers:
            headers = {"accept": "application/json",
                       "Content-Type": "application/json"}

        self.url = self.base_url + endpoint

        rs_api = requests.post(url=self.url, data=json.dumps(payload), params=params, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"POST API response: {self.rs_json}")

        return rs_api.json()

    def get(self, endpoint, payload=None, headers=None, params=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), params=params, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")

        return rs_api.json()

    def put(self, endpoint, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"PUT API response: {self.rs_json}")

        return rs_api.json()