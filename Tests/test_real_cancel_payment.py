from App.cancel_payments import *
from pytest import mark
import allure
from resources.create_payments_data import PAYMENT_ONE_RESPONSE


@mark.api_testing_real
@allure.description("Cancel a payment as an unauthorized user")
def test_real_cancel_payment_403_unauthorized():
    payment_id = PAYMENT_ONE_RESPONSE['id']
    cancel_payment(payment_id).assert_status_code(403)


@mark.xfail
@mark.api_testing_real
@allure.description("Cancel a payment as an authorized user")
def test_real_cancel_payment_201_settled():
    payment_id = PAYMENT_ONE_RESPONSE['id']
    cancel_payment(payment_id).assert_status_code(201)
