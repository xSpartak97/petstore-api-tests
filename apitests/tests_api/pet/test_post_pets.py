import pdb

from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest
import random


@pytest.mark.smoke
@pytest.mark.tcid6
# POST /pet/{petId} - updates a pet in the store with form data
def test_add_a_new_pet():
    logger.info("TEST: Create a new pet")

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

    # assertion
    assert api_info['name'] == payload['name']


@pytest.mark.smoke
@pytest.mark.tcid7
# POST /pet/{petId} - updates a pet in the store with form data
def test_update_a_pet():
    logger.info("TEST: Update a pet name and status")

    # prepare headers
    headers = {"accept": "application/json",
               "Content-Type": "application/x-www-form-urlencoded"}

    # prepare params
    pet_id = ApiHelperUtility.create_pet()
    params = {"name": "Laki", "status": "pending"}

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.post(endpoint=f'/pet/{pet_id}', params=params, headers=headers, expected_status_code=200)

    # assertion
    assert api_info['message'] == str(pet_id)


@pytest.mark.smoke
@pytest.mark.tcid8
# POST /pet/{petId} - updates a pet in the store with form data
def test_update_a_pet_with_invalid_id():
    logger.info("TEST: Update a pet with invalid ID")

    # prepare headers
    headers = {"accept": "application/json",
               "Content-Type": "application/x-www-form-urlencoded"}

    # prepare params
    params = {"name": "Laki", "status": "pending"}
    invalid_id = -12344321100123

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.post(endpoint=f'/pet/{invalid_id}', params=params, headers=headers, expected_status_code=404)

    assert api_info['message'] == 'not found'
