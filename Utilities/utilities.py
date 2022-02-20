def get_status_code(response):
    data_status_code = response.status_code
    return data_status_code


def get_json(response):
    data_json = response.json()
    return data_json


def get_plain_json(response):
    data_json = response.json
    return data_json


def get_text(response):
    data_text = response.text
    return data_text


def get_headers(response):
    data_headers = response.headers
    return data_headers


def get_cookies(response):
    data_cookies = response.cookies
    return data_cookies
