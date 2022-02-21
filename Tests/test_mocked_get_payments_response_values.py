from App.gettting_payments import *
from apiritif import http
from unittest.mock import patch, Mock
from resources.error_responses_data \
    import GENERIC_ERROR, INVALID_AUTH_CREDS_ERROR
from Utilities.utilities import *
from resources.get_payment_responses_data import *
from pytest import mark
import allure


@mark.mocked_test
@allure.description('Verify generic error response')
def test_generic_error_response():
    with patch.object(http, 'get') as get_mock:
        mock_response = Mock(json=GENERIC_ERROR)
        get_mock.return_value = mock_response
        mocked_data = get_plain_json(
            get_payments_with_status_for_customer(
                'PENDING', 'alvaro'))['error']
        mocked_error_id = mocked_data['errorId']
        mocked_error_description = mocked_data['description']
        print(f'\nErrorId displayed: {mocked_error_id}')
        print(f'Error description displayed: {mocked_error_description}')
        assert mocked_error_id == "AnErrorId"
        assert mocked_error_description == "A human description of the error."


@mark.mocked_test
@allure.description('Verify invalid authentication credentials error response')
def test_invalid_auth_credentials_error_response():
    with patch.object(http, 'get') as get_mock:
        mock_response = Mock(json=INVALID_AUTH_CREDS_ERROR)
        get_mock.return_value = mock_response
        mocked_data = get_plain_json(
            get_payments_with_status_for_customer(
                'PENDING', 'alvaro'))['error']
        mocked_error_id = mocked_data['errorId']
        mocked_error_description = mocked_data['description']
        print(f'\nErrorId displayed: {mocked_error_id}')
        print(f'Error description displayed: {mocked_error_description}')
        assert mocked_error_id == "InvalidAuthCredentials"
        assert mocked_error_description == "Invalid authentication credentials."


@mark.mocked_test
@allure.description('Verify response for SETTLED payments for customer')
def test_settled_payment():
    with patch.object(http, 'get') as get_mock:
        mock_response = Mock(json=SETTLED)
        get_mock.return_value = mock_response
        mocked_data = get_plain_json(
            get_payments_with_status_for_customer(
                'SETTLED', 'alvaro'))['data']
        mocked_status = mocked_data[0]['status']
        print(f'Payment status is {mocked_status}')
        assert mocked_status == "SETTLED"


@mark.mocked_test
@allure.description('Verify response for CANCELLED payments for customer')
def test_cancelled_payment():
    with patch.object(http, 'get') as get_mock:
        mock_response = Mock(json=CANCELLED)
        get_mock.return_value = mock_response
        mocked_data = get_plain_json(
            get_payments_with_status_for_customer(
                'CANCELLED', 'alvaro'))['data']
        mocked_status = mocked_data[0]['status']
        print(f'Payment status is {mocked_status}')
        assert mocked_status == "CANCELLED"


@mark.mocked_test
@allure.description('Verify response for FAILED payments for customer')
def test_failed_payment():
    with patch.object(http, 'get') as get_mock:
        mock_response = Mock(json=FAILED)
        get_mock.return_value = mock_response
        mocked_data = get_plain_json(
            get_payments_with_status_for_customer(
                'FAILED', 'alvaro'))['data']
        mocked_status = mocked_data[0]['status']
        print(f'Payment status is {mocked_status}')
        assert mocked_status == "FAILED"
