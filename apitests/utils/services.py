from apitests.utils.constants import BASE_URL
from urllib.parse import urljoin
import requests
PAYMENTS_URL = urljoin(BASE_URL, 'payments')


def payments_get_request():
    # Send a request to the API server and return the response.
    response = requests.get(PAYMENTS_URL)
    return response


def payments_get_request_with_filters(filters):
    # Send a request to the API server with parameters and return the response.
    response = requests.get(PAYMENTS_URL+'?'+filters)
    return response


def create_payment_post_request(body, header):
    # Send a post request with body and header with the key
    response = requests.post(PAYMENTS_URL, body, header)
    # print(response.json())
    return response


def cancel_payment_post_request(payment_id, body, header):
    url = PAYMENTS_URL+'/'+payment_id+'/cancel'
    response = requests.post(url, body, header)
    return response
