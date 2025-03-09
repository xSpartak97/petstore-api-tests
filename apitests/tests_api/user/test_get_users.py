from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest
import pdb


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


@pytest.mark.smoke
@pytest.mark.tcid18
# GET /user/login - logs user into the system
def test_login_user():
    logger.info("TEST: Login user")

    # create user by helper utility
    user = ApiHelperUtility.create_user()
    password = "string"

    # prepare params
    params = {"username": user,
              "password": password}

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.get(endpoint='/user/login', params=params, expected_status_code=200)

    assert 'logged in user session:' in api_info['message']


@pytest.mark.smoke
@pytest.mark.tcid19
# GET /user/logout - logs out current logged in user session
def test_logout_user():
    logger.info("TEST: Logout user")

    # prepare params
    params = {"username": "aqa_api",
              "password": "string"}

    # call the api
    req_helper = RequestsUtility()

    # log in user
    user_log_in = req_helper.get(endpoint='/user/login', params=params, expected_status_code=200)

    # log out user
    api_info = req_helper.get(endpoint='/user/logout', expected_status_code=200)

    assert api_info['message'] == 'ok'
