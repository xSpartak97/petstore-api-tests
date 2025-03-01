import pdb

from apitests.src.utilities.requestsUtility import RequestsUtility
import random


class ApiHelperUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_random_pet_id():
        statuses = ['available', 'pending', 'sold']
        status = {"status": random.choice(statuses)}

        # call the api
        req_helper = RequestsUtility()
        api_info = req_helper.get(endpoint='/pet/findByStatus', params=status, expected_status_code=200)
        pet_id = api_info[0]['id']

        # return ID from the api call
        return pet_id

    @staticmethod
    def create_pet():
        # prepare payload
        statuses = ['available', 'pending', 'sold']
        status = {"status": random.choice(statuses)}
        payload = {
            "id": 123,
            "category": {
                "id": 123,
                "name": "Shpitz"
            },
            "name": "Jastin",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": f"{status}"
        }

        # call the api
        req_helper = RequestsUtility()
        api_info = req_helper.post(endpoint='/pet', payload=payload, expected_status_code=200)
        pet_id = api_info['id']

        return pet_id

    @staticmethod
    def create_user():
        # prepare payload
        payload = {
            "id": 0,
            "username": "aqa_api",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }

        # call the api
        req_helper = RequestsUtility()
        api_info = req_helper.post(endpoint='/user', payload=payload, expected_status_code=200)

        return payload['username']
