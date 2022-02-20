primer_endpoint = "https://api.primer.io/payments"


def payments_endpoint():
    return f'{primer_endpoint}'


def payment_captured(payment_id):
    return f'{primer_endpoint}/{payment_id}/capture'


def payment_cancel(payment_id):
    return f'{primer_endpoint}/{payment_id}/cancel'


def payments_with_status(status):
    return f'{primer_endpoint}?status={status}'


def payments_with_customer_id(customer_id):
    return f'{primer_endpoint}?customer_id={customer_id}'


def payments_with_status_for_customer(status, customer_id):
    return f'{primer_endpoint}?status={status}&customer_id={customer_id}'


def payments_with_currency_code(currency_code):
    return f'{primer_endpoint}?currency_code={currency_code}'
