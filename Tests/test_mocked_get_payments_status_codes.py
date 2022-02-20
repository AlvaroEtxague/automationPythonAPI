from App.gettting_payments import *
from pytest import mark
import allure


@mark.mocked_test
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code 200")
def test_mocked_status_code_200(response_get_mock):
    response_get_mock.status_code = 200
    print(f'Status code is: {get_payments_status_code()} Success')
    assert get_payments_status_code() == 200


@mark.mocked_test
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code 400")
def test_status_code_400_bad_request(response_get_mock):
    response_get_mock.status_code = 400
    print(f'Status code is: {get_payments_status_code()} Bad Request')
    assert get_payments_status_code() == 400


@mark.mocked_test
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code 401")
def test_status_code_401_unauthorized(response_get_mock):
    response_get_mock.status_code = 401
    print(f'Status code is: {get_payments_status_code()} Unauthorized')
    assert get_payments_status_code() == 401


@mark.mocked_test
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code 403")
def test_status_code_403_forbidden(response_get_mock):
    response_get_mock.status_code = 403
    print(f'Status code is: {get_payments_status_code()} Forbidden')
    assert get_payments_status_code() == 403


@mark.mocked_test
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code 404")
def test_status_code_404_entity_not_found(response_get_mock):
    response_get_mock.status_code = 404
    print(f'Status code is: {get_payments_status_code()} Entity Not Found')
    assert get_payments_status_code() == 404


@mark.mocked_test
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code 409")
def test_status_code_409_entity_already_exists(response_get_mock):
    response_get_mock.status_code = 409
    print(
        f'Status code is: {get_payments_status_code()} Entity Already Exists')
    assert get_payments_status_code() == 409


@mark.mocked_test
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code 422")
def test_status_code_422_input_validation_failed(response_get_mock):
    response_get_mock.status_code = 422
    print(
        f'Status code is: {get_payments_status_code()} Input Validation Failed')
    assert get_payments_status_code() == 422
