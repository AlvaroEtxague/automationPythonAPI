from App.capture_payment import *
from pytest import mark
import allure


@mark.api_testing_real
@allure.description("Capture a payment as an unauthorized user")
def test_real_capture_payment_403_unauthorized():
    payment_id = PAYMENT_ONE_RESPONSE['id']
    capture_payment(payment_id).assert_status_code(403)


@mark.api_testing_real
@allure.description("Capture a payment as an authorized user")
@mark.xfail
def test_real_capture_payment_200_settled():
    payment_id = PAYMENT_ONE_RESPONSE['id']
    capture_payment(payment_id).assert_status_code(200)
