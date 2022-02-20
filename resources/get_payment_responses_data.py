PENDING = {
	"data": [{
		"id": "IHQlakKC",
		"date": "2021-03-24T14:56:56.869248",
		"status": "PENDING",
		"orderId": "my-order-122",
		"currencyCode": "EUR",
		"amount": 700,
		"processor": {
			"name": "STRIPE",
			"processorMerchantId": "acct_stripe_1234"
		},
		"metadata": {
			"productId": 122,
			"merchantId": "a13bsd62s"
		}
	}],
	"nextCursor": "string",
	"prevCursor": "string"
}

FAILED = {
	"data": [{
		"id": "IHQlakKC",
		"date": "2021-03-24T14:56:56.869248",
		"status": "FAILED",
		"orderId": "my-order-123",
		"currencyCode": "USD",
		"amount": 100,
		"processor": {
			"name": "STRIPE",
			"processorMerchantId": "acct_stripe_1234"
		},
		"metadata": {
			"productId": 123,
			"merchantId": "a13bsd62s"
		}
	}],
	"nextCursor": "string",
	"prevCursor": "string"
}

AUTHORIZED = {
	"data": [{
		"id": "IHQlakKC",
		"date": "2021-03-24T14:56:56.869248",
		"status": "AUTHORIZED",
		"orderId": "my-order-124",
		"currencyCode": "AUD",
		"amount": 200,
		"processor": {
			"name": "STRIPE",
			"processorMerchantId": "acct_stripe_1234"
		},
		"metadata": {
			"productId": 124,
			"merchantId": "a13bsd62s"
		}
	}],
	"nextCursor": "string",
	"prevCursor": "string"
}

DECLINED = {
	"data": [{
		"id": "IHQlakKC",
		"date": "2021-03-24T14:56:56.869248",
		"status": "DECLINED",
		"orderId": "my-order-125",
		"currencyCode": "EUR",
		"amount": 300,
		"processor": {
			"name": "STRIPE",
			"processorMerchantId": "acct_stripe_1234"
		},
		"metadata": {
			"productId": 125,
			"merchantId": "a13bsd62s"
		}
	}],
	"nextCursor": "string",
	"prevCursor": "string"
}

CANCELLED = {
	"data": [{
		"id": "IHQlakKC",
		"date": "2021-03-24T14:56:56.869248",
		"status": "CANCELLED",
		"orderId": "my-order-126",
		"currencyCode": "EUR",
		"amount": 400,
		"processor": {
			"name": "STRIPE",
			"processorMerchantId": "acct_stripe_1234"
		},
		"metadata": {
			"productId": 126,
			"merchantId": "a13bsd62s"
		}
	}],
	"nextCursor": "string",
	"prevCursor": "string"
}

SETTLED = {
	"data": [{
		"id": "IHQlakKC",
		"date": "2021-03-24T14:56:56.869248",
		"status": "SETTLED",
		"orderId": "my-order-127",
		"currencyCode": "EUR",
		"amount": 500,
		"processor": {
			"name": "STRIPE",
			"processorMerchantId": "acct_stripe_1234"
		},
		"metadata": {
			"productId": 127,
			"merchantId": "a13bsd62s"
		}
	}],
	"nextCursor": "string",
	"prevCursor": "string"
}
