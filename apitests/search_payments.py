from nose.tools import assert_true, assert_equal, assert_dict_equal, assert_false
import unittest
from apitests.utils.constants import payments_api_response_simple, \
    payments_api_response_filtered
from apitests.utils.services import payments_get_request, payments_get_request_with_filters
from unittest.mock import patch


class SearchPaymentsApiTests(unittest.TestCase):

    @staticmethod
    def test_real_get_payment_endpoint():
        # testing the real api here. Expecting no_auth response
        # Send a request to the API server and store the response.
        response = payments_get_request()
        assert_equal(response.status_code, 401)

    @staticmethod
    @patch('apitests.utils.services.requests.get')
    # by patching we intercept the request with a mock service
    def test_mock_get_payments_ok(mock_get):
        # Configure the mock to return a response with
        # an OK status and a specific json body
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = payments_api_response_simple

        # Send a request to the API
        response = payments_get_request()

        # Confirm desired response and print the status
        assert_true(response.ok)
        assert_dict_equal(response.json(), payments_api_response_simple)
        payment_status = response.json()['data'][0]['status']

    @staticmethod
    @patch('apitests.utils.services.requests.get')
    def test_mock_get_payments_not_ok(mock_get):
        # Testing the case of a non-OK response
        mock_get.return_value.ok = False
        response = payments_get_request()
        assert_false(response.ok)

    @staticmethod
    @patch('apitests.utils.services.requests.get')
    def test_mock_get_payment_with_params(mock_get):
        # Retrieve payments after a certain date
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = payments_api_response_filtered

        response = payments_get_request_with_filters('from_date=2021-03-01T14:56:56.869248')

        assert_true(response.ok)
        assert_dict_equal(response.json(), payments_api_response_filtered)

    @staticmethod
    @patch('apitests.utils.services.requests.get')
    def test_mock_get_settled_payment_with_params(mock_get):
        # Retrieve SETTLED payments after a certain date
        failed_payments_number = 0
        query_parameters = 'from_date=2021-03-01T14:56:56.869248'
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = payments_api_response_filtered

        response = payments_get_request_with_filters(query_parameters)

        assert_true(response.ok)
        # simple logic to count SETTLED payments of the results object
        data_length = len(response.json()['data'])
        for x in range(data_length):
            if response.json()['data'][x]['status'] == 'SETTLED':
                failed_payments_number += 1
        print('There are ' + str(data_length) + ' payments after this date.' + str(
            failed_payments_number) + ' is/are SETTLED')

    """We can have test cases for paginated responses as well
    that would go through as many pages as per our needs"""


if __name__ == '__main__':
    unittest.main()
