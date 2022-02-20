from unittest.mock import patch, Mock
import allure
from pytest import mark
from App.capture_payment import *
from App.gettting_payments import *
from Utilities.utilities import get_plain_json
from resources.capture_payment_data import *


@mark.mocked_test
@allure.description(
    "Capture a payment as an authorized user"
    " and verify that the status is SETTLED")
def test_mocked_capture_payment_200_settled():
    payment_id = PAYMENT_ONE_RESPONSE['id']
    with patch.object(http, 'post') as mock_post:
        mock_response = Mock(
            status_code=200,
            json=CAPTURE_PAYMENT_RESPONSE_SETTLED
        )
        mock_post.return_value = mock_response
        mocked_data = get_plain_json(capture_payment(payment_id))
        mocked_status = mocked_data['status']
        mocked_id = mocked_data['id']
        assert mock_response.status_code == 200
        assert mocked_status == 'SETTLED'
        assert mocked_id == payment_id


@allure.description(
    "Capture a payment as an authorized user"
    " and verify that the status is SETTLING")
def test_mocked_capture_payment_200_settling():
    payment_id = PAYMENT_ONE_RESPONSE['id']
    with patch.object(http, 'post') as mock_post:
        mock_response = Mock(
            status_code=200,
            json=CAPTURE_PAYMENT_RESPONSE_SETTLING
        )
        mock_post.return_value = mock_response
        mocked_data = get_plain_json(capture_payment(payment_id))
        mocked_status = mocked_data['status']
        mocked_id = mocked_data['id']
        assert mock_response.status_code == 200
        assert mocked_status == 'SETTLING'
        assert mocked_id == payment_id
