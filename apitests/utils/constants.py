BASE_URL = 'https://api.sandbox.primer.io'
# get requests
payments_api_response_simple = {
  "data": [
    {
      "id": "IHQlakKC",
      "date": "2021-03-24T14:56:56.869248",
      "status": "SETTLED",
      "orderId": "my-order-123",
      "currencyCode": "EUR",
      "amount": 700,
      "processor": {
        "name": "STRIPE",
        "processorMerchantId": "acct_stripe_1234"
      },
      "metadata": {
        "productId": 123,
        "merchantId": "a13bsd62s"
      }
    }
  ],
  "nextCursor": "string",
  "prevCursor": "string"
}
payments_api_response_filtered = {
  "data": [
    {
      "id": "IHQjepKC",
      "date": "2021-03-24T14:56:56.869248",
      "status": "SETTLED",
      "orderId": "my-order-123",
      "currencyCode": "EUR",
      "amount": 700,
      "processor": {
        "name": "STRIPE",
        "processorMerchantId": "acct_stripe_1234"
      },
      "metadata": {
        "productId": 123,
        "merchantId": "a13bsd62s"
      }
    },
    {
      "id": "IHQlakKC",
      "date": "2021-03-28T14:56:56.869248",
      "status": "SETTLED",
      "orderId": "my-order-100",
      "currencyCode": "EUR",
      "amount": 7000,
      "processor": {
        "name": "STRIPE",
        "processorMerchantId": "acct_stripe_1234"
      },
      "metadata": {
        "productId": 100,
        "merchantId": "a13bsk42s"
      }
    },
    {
      "id": "IwujakKC",
      "date": "2021-04-28T14:56:56.869248",
      "status": "FAILED",
      "orderId": "my-order-101",
      "currencyCode": "EUR",
      "amount": 90000,
      "processor": {
        "name": "STRIPE",
        "processorMerchantId": "acct_stripe_1234"
      },
      "metadata": {
        "productId": 101,
        "merchantId": "aas3sk42s"
      }
    }
  ],
  "nextCursor": "string",
  "prevCursor": "string"
}
# post requests
create_payment_request_body = {
  "customerId": "customer-123",
  "orderId": "order-abc",
  "currencyCode": "EUR",
  "amount": 42,
  "paymentMethodToken": "heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4",
  "paymentMethod": {
    "vaultOnSuccess": 'true'
  },
  "customer": {
    "emailAddress": "customer123@gmail.com"
  },
  "metadata": {
    "productId": 123,
    "merchantId": "a13bsd62s"
  }
}
create_payment_response_body = {
  "id": "kHdEw9EG",
  "date": "2021-02-21T15:36:16.367687",
  "status": "AUTHORIZED",
  "orderId": "order-abc",
  "customerId": "customer-123",
  "currencyCode": "EUR",
  "amount": 42,
  "paymentMethod": {
    "paymentMethodToken": "heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4",
    "vaultedPaymentMethodToken": "_xlXlmBcTnuFxc2N3HAI73wxNjE1NTU5ODY5",
    "descriptor": "Purchase: Socks",
    "analyticsId": "VtkMDAxZW5isH0HsbbNxZ3lo",
    "paymentMethodType": "PAYMENT_CARD",
    "paymentMethodData": {
      "first6Digits": "411111",
      "last4Digits": "1111",
      "expirationMonth": "12",
      "expirationYear": "2030",
      "cardholderName": "John Biggins",
      "network": "Visa",
      "isNetworkTokenized": 'false',
      "binData": {
        "network": "VISA",
        "regionalRestriction": "UNKNOWN",
        "accountNumberType": "UNKNOWN",
        "accountFundingType": "UNKNOWN",
        "prepaidReloadableIndicator": "NOT_APPLICABLE",
        "productUsageType": "UNKNOWN",
        "productCode": "VISA",
        "productName": "VISA"
      }
    }
  },
  "processor": {
    "name": "STRIPE",
    "processor_merchant_id": "acct_stripe_1234",
    "amountCaptured": 0,
    "amountRefunded": 0
  },
  "transactions": [
    {
      "type": "SALE",
      "processorStatus": "AUTHORIZED",
      "processorName": "STRIPE",
      "processorMerchantId": "acct_stripe_1234",
      "processorTransactionId": "54c4eb5b3ef8a"
    }
  ],
  "customer": {
    "email": "customer123@gmail.com"
  },
  "metadata": {
    "productId": 123,
    "merchantId": "a13bsd62s"
  }
}
headers = 'key'
cancel_reason = {'message': 'The guitar I ordered is damaged'}
cancel_payment_response_body = {
  "id": "kHdEw9EG",
  "date": "2021-02-21T15:36:16.367687",
  "status": "CANCELLED",
  "orderId": "order-abc",
  "customerId": "customer-123",
  "currencyCode": "EUR",
  "amount": 42,
  "paymentMethod": {
    "paymentMethodToken": "heNwnqaeRiqvY1UcslfQc3wxNjEzOTIxNjc4",
    "vaultedPaymentMethodToken": "_xlXlmBcTnuFxc2N3HAI73wxNjE1NTU5ODY5",
    "descriptor": "Purchase: Socks",
    "analyticsId": "VtkMDAxZW5isH0HsbbNxZ3lo",
    "paymentMethodType": "PAYMENT_CARD",
    "paymentMethodData": {
      "first6Digits": "411111",
      "last4Digits": "1111",
      "expirationMonth": "12",
      "expirationYear": "2030",
      "cardholderName": "John Biggins",
      "network": "Visa",
      "isNetworkTokenized": 'false',
      "binData": {
        "network": "VISA",
        "regionalRestriction": "UNKNOWN",
        "accountNumberType": "UNKNOWN",
        "accountFundingType": "UNKNOWN",
        "prepaidReloadableIndicator": "NOT_APPLICABLE",
        "productUsageType": "UNKNOWN",
        "productCode": "VISA",
        "productName": "VISA"
      }
    }
  },
  "processor": {
    "name": "STRIPE",
    "processor_merchant_id": "acct_stripe_1234",
    "amountCaptured": 0,
    "amountRefunded": 0
  },
  "transactions": [
    {
      "type": "SALE",
      "processorStatus": "CANCELLED",
      "processorName": "STRIPE",
      "processorMerchantId": "acct_stripe_1234",
      "processorTransactionId": "54c4eb5b3ef8a"
    }
  ],
  "customer": {
    "email": "customer123@gmail.com"
  },
  "metadata": {
    "productId": 123,
    "merchantId": "a13bsd62s"
  }
}
