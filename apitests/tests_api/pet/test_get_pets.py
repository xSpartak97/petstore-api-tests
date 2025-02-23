from apitests.src.utilities.requestsUtility import RequestsUtility
import logging as logger
import pytest

import pdb
import requests


@pytest.mark.smoke
@pytest.mark.tcid1
def test_get_pet_by_status():
    logger.info("TEST: Get pet by status (available)")

    # call the api
    req_helper = RequestsUtility()

    params = {"status": "available"}

    # call the api
    api_info = req_helper.get(endpoint='/pet/findByStatus', params=params, expected_status_code=200)
    data = api_info[:1]

    # assertion
    assert data[0]['status'] == params['status']
