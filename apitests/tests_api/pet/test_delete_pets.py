from apitests.src.utilities.requestsUtility import RequestsUtility
from apitests.src.utilities.apihelperUtility import ApiHelperUtility
import logging as logger
import pytest


@pytest.mark.smoke
@pytest.mark.tcid11
# DELETE /pet/{petId} - deletes a pet
def test_delete_a_pet():
    logger.info("TEST: Delete an existing pet")

    # get random pet id
    random_pet_id = ApiHelperUtility.get_random_pet_id()

    # call the api
    req_helper = RequestsUtility()
    api_info = req_helper.delete(f"/pet/{random_pet_id}")

    assert str(random_pet_id) == api_info['message']
