from unittest.mock import patch, Mock
from App.cancel_payments import cancel_payment
from App.gettting_payments import *
from Utilities.utilities import get_plain_json
from resources.cancel_payment_data import *
import allure
from pytest import mark


@mark.mocked_test
@allure.description("Cancel a payment as an authorized user")
def test_mocked_cancel_payment_200():
    payment_id = PAYMENT_ONE_RESPONSE['id']
    with patch.object(http, 'post') as mock_post:
        mock_response = Mock(
            status_code=200,
            json=CANCEL_PAYMENT_RESPONSE
        )
        mock_post.return_value = mock_response
        mocked_data = get_plain_json(cancel_payment(payment_id))
        mocked_status = mocked_data['status']
        mocked_id = mocked_data['id']
        assert mock_response.status_code == 200
        assert mocked_status == 'CANCELLED'
        assert mocked_id == payment_id
