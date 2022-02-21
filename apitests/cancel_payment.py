import unittest
from unittest.mock import patch
from apitests.utils.constants import headers, cancel_reason, cancel_payment_response_body
from apitests.utils.services import cancel_payment_post_request
from nose.tools import assert_true, assert_equal, assert_dict_equal, assert_false


class CancelPaymentApiTests(unittest.TestCase):

    @staticmethod
    def test_real_post_cancel_payment_endpoint():
        # testing the real api here. Expecting forbidden response
        # Send a request to the API server and store the response.
        response = cancel_payment_post_request('IHQlakKC', cancel_reason, headers)
        assert_equal(response.status_code, 403)
        assert_equal(response.json()['message'], 'Forbidden')
        assert_false(response.ok)

    @staticmethod
    @patch('apitests.utils.services.requests.post')
    def test_mock_cancel_payment(mock_post):
        # Testing that after canceling a payment we have correct status
        mock_post.return_value.ok = True
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = cancel_payment_response_body

        response = cancel_payment_post_request('IHQlakKC', cancel_reason, headers)
        assert_true(response.ok)
        assert_equal(response.status_code, 200)
        assert_dict_equal(response.json(), cancel_payment_response_body)
        assert_equal(response.json()['status'], 'CANCELLED')

    @staticmethod
    @patch('apitests.utils.services.requests.post')
    def test_mock_cancel_payment_bad_request(mock_post):
        # Testing a bad request response
        mock_post.return_value.ok = False
        mock_post.return_value.status_code = 400
        mock_post.return_value.json.return_value = {'message': 'Bad Request'}

        response = cancel_payment_post_request('IHQlakKC', cancel_reason, headers)
        assert_false(response.ok)
        assert_equal(response.status_code, 400)
        assert_equal(response.json()['message'], 'Bad Request')


if __name__ == '__main__':
    unittest.main()
