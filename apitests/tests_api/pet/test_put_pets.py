from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest
import pdb


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
