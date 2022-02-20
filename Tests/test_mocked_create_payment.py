from unittest.mock import patch, Mock
import allure
from pytest import mark
from App.gettting_payments import *
from Utilities.utilities import get_plain_json


@mark.mocked_test
@allure.description("Create a payment as an authorized user")
def test_mocked_create_payment_200_authorized():
    with patch.object(http, 'post') as mock_post:
        mock_response = Mock(status_code=200, json=PAYMENT_ONE_RESPONSE)
        mock_post.return_value = mock_response
        mocked_data = get_plain_json(create_payment())
        mocked_status = mocked_data['status']
        assert mock_response.status_code == 200
        assert mocked_status == 'AUTHORIZED'
