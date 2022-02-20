from App.gettting_payments import *
from pytest import mark
import allure


@mark.api_testing_real
@allure.description(
    "Fetch https://api.primer.io/payments and verify status code is 401")
def test_real_status_code_401_unauthorized():
    get_payments().assert_status_code(401)


@mark.api_testing_real
@allure.description("Fetch declined payments for specific customer")
def test_real_declined_payments_for_customer():
    get_payments_with_status_for_customer('DECLINED', 'alvaro').assert_status_code(401)


@mark.api_testing_real
@allure.description("Fetch all euro payments")
def test_real_euro_payments():
    get_payments_with_currency_code('EUR').assert_status_code(401)
