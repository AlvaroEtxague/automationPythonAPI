from App.gettting_payments import *
from Utilities.utilities import *
from resources.error_responses_data import INVALID_AUTH_CREDS_ERROR
from pytest import mark
import allure


@mark.api_testing_real
@allure.description(
    "Fetch pending payments for specific customer and verify error responses")
def test_real_invalid_auth_credentials_error_response():
    response = get_json(
        get_payments_with_status_for_customer('PENDING', 'alvaro'))
    error_id = response['error']['errorId']
    error_description = response['error']['description']
    assert error_id == INVALID_AUTH_CREDS_ERROR['error']['errorId']
    assert error_description == INVALID_AUTH_CREDS_ERROR['error']['description']
