from apiritif import http
from App.creating_payments import *
from Utilities.utilities import get_status_code


headers = {
    'Content-Type': 'text/plain',
    'X-Api-Key': 'fake-key',
    'X-Idempotency-Key': 'X-Idempotency-Key-test'
}


def get_payments():
    response = http.get(url.payments_endpoint(), headers=headers)
    return response


def get_payments_status_code():
    response = http.get(url.payments_endpoint(), headers=headers)
    return get_status_code(response)


def get_payments_with_status_for_customer(status, customer):
    response = http.get(
        url.payments_with_status_for_customer(status, customer),
        headers=headers)
    return response


def get_payments_with_currency_code(currency_code):
    response = http.get(
        url.payments_with_currency_code(currency_code),
        headers=headers)
    return response


def get_payments_status_code():
    response = http.get(
        url.payments_endpoint(),
        headers=headers)
    return get_status_code(response)
