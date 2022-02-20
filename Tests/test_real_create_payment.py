from App.gettting_payments import *
from pytest import mark
import allure


@mark.api_testing_real
@allure.description("Create a payment as an unauthorized user")
def test_real_create_payment_403_unauthorized():
    print(create_payment().text)
    create_payment().assert_status_code(403)
