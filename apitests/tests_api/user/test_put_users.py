from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest


@pytest.mark.smoke
@pytest.mark.tcid15
# PUT /user/{username} - updated user
def test_update_user():
    logger.info("TEST: Update existed user")

    # prepare payload
    user_name = ApiHelperUtility.create_user()
    payload = {
        "id": 1,
        "username": "aqa_api_updated",
        "firstName": "api",
        "lastName": "test",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.put(endpoint=f'/user/{user_name}', payload=payload, expected_status_code=200)

    assert api_info


@pytest.mark.smoke
@pytest.mark.tcid16
# PUT /user/{username} - updated user
def test_update_user_invalid_id():
    logger.info("TEST: Update existed user with invalid ID")

    # prepare payload
    user_name = ApiHelperUtility.create_user()
    payload = {
        "id": "unknown",
        "username": "aqa_api_updated",
        "firstName": "api",
        "lastName": "test",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.put(endpoint=f'/user/{user_name}', payload=payload, expected_status_code=500)

    assert api_info['message'] == 'something bad happened'
