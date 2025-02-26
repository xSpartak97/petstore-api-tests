from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest


@pytest.mark.smoke
@pytest.mark.parametrize("status",
                         [pytest.param('available', marks=pytest.mark.tcid1),
                          pytest.param('pending', marks=pytest.mark.tcid2),
                          pytest.param('sold', marks=pytest.mark.tcid3)
                          ])
def test_get_pet_by_status(status):
    logger.info("TEST: Get pet by status")

    # prepare parameters
    params = {"status": status}

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.get(endpoint='/pet/findByStatus', params=params, expected_status_code=200)
    data = api_info[:1]

    # assertion
    assert data[0]['status'] == params['status'], f"The requested status does not match the found status." \
                                                  f"Actual: {data[0]['status']}" \
                                                  f"Expected: {params['status']}"


@pytest.mark.smoke
@pytest.mark.tcid4
def test_find_pet_by_id():
    logger.info("TEST: Find pet by ID")

    # call the api
    req_helper = RequestsUtility()
    pet_id = ApiHelperUtility.get_random_pet_id()

    api_info = req_helper.get(endpoint=f'/pet/{pet_id}', expected_status_code=200)

    # assertion
    assert api_info['id'] == pet_id, f"The requested status does not match the found status." \
                                     f"Actual ID: {api_info['id']}" \
                                     f"Expected ID: {pet_id}"


@pytest.mark.smoke
@pytest.mark.tcid5
def test_find_pet_by_invalid_id():
    logger.info("TEST: Find pet by invalid ID")

    # call the api
    req_helper = RequestsUtility()
    invalid_id = -12344321100123

    api_info = req_helper.get(endpoint=f'/pet/{invalid_id}', expected_status_code=404)

    # assertion
    assert api_info['message'] == 'Pet not found'

