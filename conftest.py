from unittest.mock import patch, Mock
from pytest import fixture
from App.gettting_payments import *


@fixture(scope="function")
def response_get_mock():
    with patch.object(http, 'get') as get_mock:
        mock_response = Mock()
        get_mock.return_value = mock_response
        yield mock_response


@fixture(scope="function")
def response_get_mock_with_json():
    def my_json_mock(json_dict):
        with patch.object(http, 'get') as get_mock:
            mock_response = Mock(json=json_dict)
            get_mock.return_value = mock_response
            return mock_response
    yield my_json_mock
