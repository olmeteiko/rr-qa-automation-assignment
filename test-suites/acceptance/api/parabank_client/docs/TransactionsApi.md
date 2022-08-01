# swagger_client.TransactionsApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_transaction1**](TransactionsApi.md#get_transaction1) | **GET** /transactions/{transactionId} | Get the transaction for the id
[**get_transactions1**](TransactionsApi.md#get_transactions1) | **GET** /accounts/{accountId}/transactions | Get the list of Transactions for the account
[**get_transactions_by_amount1**](TransactionsApi.md#get_transactions_by_amount1) | **GET** /accounts/{accountId}/transactions/amount/{amount} | Create transactions by amount for account
[**get_transactions_by_month_and_type1**](TransactionsApi.md#get_transactions_by_month_and_type1) | **GET** /accounts/{accountId}/transactions/month/{month}/type/{type} | Fetch transactions by month and type for account
[**get_transactions_by_to_from_date1**](TransactionsApi.md#get_transactions_by_to_from_date1) | **GET** /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate} | Fetch transactions for date range for account
[**get_transactions_on_date1**](TransactionsApi.md#get_transactions_on_date1) | **GET** /accounts/{accountId}/transactions/onDate/{onDate} | Fetch transactions for a specific date for account


# **get_transaction1**
> Transaction get_transaction1(transaction_id)

Get the transaction for the id



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
transaction_id = 56 # int | Unique identifier for the transaction

try:
    # Get the transaction for the id
    api_response = api_instance.get_transaction1(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| Unique identifier for the transaction | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions1**
> list[Transaction] get_transactions1(account_id)

Get the list of Transactions for the account



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
account_id = 56 # int | Account id

try:
    # Get the list of Transactions for the account
    api_response = api_instance.get_transactions1(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account id | 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_amount1**
> list[Transaction] get_transactions_by_amount1(account_id, amount)

Create transactions by amount for account



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
account_id = 56 # int | Account id
amount = 8.14 # float | Amount

try:
    # Create transactions by amount for account
    api_response = api_instance.get_transactions_by_amount1(account_id, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_amount1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account id | 
 **amount** | **float**| Amount | 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_month_and_type1**
> list[Transaction] get_transactions_by_month_and_type1(account_id, month, type)

Fetch transactions by month and type for account



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
account_id = 56 # int | Account id
month = 'month_example' # str | Month to use for the search range
type = 'type_example' # str | Transaction type (CREDIT, DEBIT)

try:
    # Fetch transactions by month and type for account
    api_response = api_instance.get_transactions_by_month_and_type1(account_id, month, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_month_and_type1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account id | 
 **month** | **str**| Month to use for the search range | 
 **type** | **str**| Transaction type (CREDIT, DEBIT) | 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_by_to_from_date1**
> list[Transaction] get_transactions_by_to_from_date1(account_id, from_date, to_date)

Fetch transactions for date range for account



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
account_id = 56 # int | Account id
from_date = 'from_date_example' # str | Search starting date
to_date = 'to_date_example' # str | Search ending date

try:
    # Fetch transactions for date range for account
    api_response = api_instance.get_transactions_by_to_from_date1(account_id, from_date, to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_by_to_from_date1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account id | 
 **from_date** | **str**| Search starting date | 
 **to_date** | **str**| Search ending date | 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_on_date1**
> list[Transaction] get_transactions_on_date1(account_id, on_date)

Fetch transactions for a specific date for account



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TransactionsApi()
account_id = 56 # int | Account id
on_date = 'on_date_example' # str | Search specific date

try:
    # Fetch transactions for a specific date for account
    api_response = api_instance.get_transactions_on_date1(account_id, on_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions_on_date1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account id | 
 **on_date** | **str**| Search specific date | 

### Return type

[**list[Transaction]**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

