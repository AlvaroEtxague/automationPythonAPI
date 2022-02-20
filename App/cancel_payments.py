from apiritif import http
from App import endpoints as url
from resources.cancel_payment_data import *


def cancel_payment(payment_id):
    payload = CANCEL_PAYMENT_PAYLOAD
    headers = {
        'Content-Type': 'text/plain',
        'X-Api-Key': 'fake-key',
        'X-Idempotency-Key': 'X-Idempotency-Key-test'
    }
    response = http.post(
        url.payment_cancel(payment_id),
        headers=headers,
        data=payload,
    )
    return response
