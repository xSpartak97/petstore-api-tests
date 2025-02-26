from apitests.src.utilities.requestsUtility import RequestsUtility
import logging as logger
import pytest


@pytest.mark.smoke
@pytest.mark.tcid12
# POST /user - crete user
def test_add_new_user():
    logger.info("TEST: Create a new user")

    # prepare payload
    payload = {
        "id": 0,
        "username": "string",
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

    # assertion
    assert api_info['code'] == 200


@pytest.mark.smoke
@pytest.mark.tcid13
# POST /user - crete user
def test_add_new_user_without_body():
    logger.info("TEST: Create a new user without body")

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.post(endpoint='/user', expected_status_code=405)

    assert api_info['code'] == 405
    assert api_info['message'] == 'no data'
