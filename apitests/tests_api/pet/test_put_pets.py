from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
from apitests.src.utilities import dataUtility
import logging as logger
import pytest


@pytest.mark.smoke
@pytest.mark.tcid9
# PUT /pet - update an existing pet
def test_update_a_pet():
    logger.info("TEST: Update an existing pet")

    # payload prepare
    random_pet_id = ApiHelperUtility.get_random_pet_id()
    payload = {
        "id": random_pet_id,
        "category": {
            "id": 0,
            "name": "api_test"
        },
        "name": "api_test",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.put(endpoint='/pet', payload=payload, expected_status_code=200)

    # assertion
    assert api_info['name'] == payload['name']


@pytest.mark.smoke
@pytest.mark.xfail
@pytest.mark.tcid10
# PUT /pet - update an existing pet
def test_update_a_pet_with_invalid_id():
    logger.info("TEST: Update an existing pet with invalid pet ID")

    # payload prepare
    payload = dataUtility.request_json_file('petInvalidData.json')

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.put(endpoint='/pet', payload=payload, expected_status_code=404)
    pdb.set_trace()
    # assertion
    assert api_info['message'] == payload['Pet not found']
