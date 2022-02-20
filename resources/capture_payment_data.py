CAPTURE_PAYMENT_PAYLOAD = {
  "final": True,
  "amount": 42
}


CAPTURE_PAYMENT_RESPONSE_SETTLED = {
  "id": "kHdEw9EG",
  "date": "2021-02-21T15:36:16.367687",
  "status": "SETTLED",
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
      "isNetworkTokenized": False,
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
    "amountCaptured": 42,
    "amountRefunded": 0
  },
  "transactions": [
    {
      "type": "SALE",
      "processorStatus": "SETTLED",
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

CAPTURE_PAYMENT_RESPONSE_SETTLING = {
  "id": "kHdEw9EG",
  "date": "2021-02-21T15:36:16.367687",
  "status": "SETTLING",
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
      "isNetworkTokenized": False,
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
    "amountCaptured": 42,
    "amountRefunded": 0
  },
  "transactions": [
    {
      "type": "SALE",
      "processorStatus": "SETTLED",
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
