from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest


@pytest.mark.smoke
@pytest.mark.tcid17
# DELETE /user/{username} - delete user
def test_delete_user():
    logger.info("TEST: Delete user")

    # prepare params
    user_name = ApiHelperUtility.create_user()

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.delete(endpoint=f'/user/{user_name}', expected_status_code=200)

    # assertion
    assert api_info['message'] == user_name
