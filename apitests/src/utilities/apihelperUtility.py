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
        random_id = random.randint(0, len(api_info[:100]) - 1)

        # return random ID from the api call
        return int(api_info[random_id]['id'])
