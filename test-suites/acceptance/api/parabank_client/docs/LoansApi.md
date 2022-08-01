# swagger_client.LoansApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_loan1**](LoansApi.md#request_loan1) | **POST** /requestLoan | Request a loan


# **request_loan1**
> LoanResponse request_loan1(customer_id, amount, down_payment, from_account_id)

Request a loan



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LoansApi()
customer_id = 56 # int | Customer's id
amount = 8.14 # float | Amount
down_payment = 8.14 # float | Downpayment for the loan
from_account_id = 56 # int | Customer funds source account

try:
    # Request a loan
    api_response = api_instance.request_loan1(customer_id, amount, down_payment, from_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoansApi->request_loan1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 
 **amount** | **float**| Amount | 
 **down_payment** | **float**| Downpayment for the loan | 
 **from_account_id** | **int**| Customer funds source account | 

### Return type

[**LoanResponse**](LoanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

