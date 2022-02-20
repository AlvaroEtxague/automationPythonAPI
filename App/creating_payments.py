from apiritif import http
from App import endpoints as url
from resources.create_payments_data import *


def create_payment():
    payload = PAYMENT_ONE_PAYLOAD
    headers = {
        'Content-Type': 'text/plain',
        'X-Api-Key': 'fake-key',
        'X-Idempotency-Key': 'X-Idempotency-Key-test'
    }
    response = http.post(
        url.payments_endpoint(),
        headers=headers,
        data=payload)
    return response
