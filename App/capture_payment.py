from apiritif import http
from App import endpoints as url
from resources.create_payments_data import *


def capture_payment(payment_id):
    payload = PAYMENT_ONE_RESPONSE
    headers = {
        'Content-Type': 'text/plain',
        'X-Api-Key': 'fake-key',
        'X-Idempotency-Key': 'X-Idempotency-Key-test'
    }
    response = http.post(
        url.payment_captured(payment_id),
        headers=headers,
        data=payload,
    )
    return response
