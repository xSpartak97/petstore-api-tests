from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest


@pytest.mark.smoke
@pytest.mark.tcid14
# GET /user/{username} - get user by username
def test_get_user():
    logger.info("TEST: Get user by username")

    # create user by helper utility
    user_name = ApiHelperUtility.create_user()

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.get(endpoint=f'/user/{user_name}', expected_status_code=200)

    assert api_info['username'] == user_name
