# swagger_client.AccountsApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bill_pay1**](AccountsApi.md#bill_pay1) | **POST** /billpay | Pay bill
[**create_account1**](AccountsApi.md#create_account1) | **POST** /createAccount | Create a new account
[**deposit1**](AccountsApi.md#deposit1) | **POST** /deposit | Deposit funds
[**get_account1**](AccountsApi.md#get_account1) | **GET** /accounts/{accountId} | Get Account by Id
[**get_accounts1**](AccountsApi.md#get_accounts1) | **GET** /customers/{customerId}/accounts | Get Customer Accounts
[**get_transactions1**](AccountsApi.md#get_transactions1) | **GET** /accounts/{accountId}/transactions | Get the list of Transactions for the account
[**get_transactions_by_amount1**](AccountsApi.md#get_transactions_by_amount1) | **GET** /accounts/{accountId}/transactions/amount/{amount} | Create transactions by amount for account
[**get_transactions_by_month_and_type1**](AccountsApi.md#get_transactions_by_month_and_type1) | **GET** /accounts/{accountId}/transactions/month/{month}/type/{type} | Fetch transactions by month and type for account
[**get_transactions_by_to_from_date1**](AccountsApi.md#get_transactions_by_to_from_date1) | **GET** /accounts/{accountId}/transactions/fromDate/{fromDate}/toDate/{toDate} | Fetch transactions for date range for account
[**get_transactions_on_date1**](AccountsApi.md#get_transactions_on_date1) | **GET** /accounts/{accountId}/transactions/onDate/{onDate} | Fetch transactions for a specific date for account
[**transfer1**](AccountsApi.md#transfer1) | **POST** /transfer | Transfer funds
[**withdraw1**](AccountsApi.md#withdraw1) | **POST** /withdraw | Withdraw funds


# **bill_pay1**
> BillPayResult bill_pay1(account_id, amount, body)

Pay bill



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Bill payment source account
amount = 8.14 # float | Amount
body = swagger_client.Payee() # Payee | Payee

try:
    # Pay bill
    api_response = api_instance.bill_pay1(account_id, amount, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->bill_pay1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Bill payment source account | 
 **amount** | **float**| Amount | 
 **body** | [**Payee**](Payee.md)| Payee | 

### Return type

[**BillPayResult**](BillPayResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account1**
> Account create_account1(customer_id, new_account_type, from_account_id)

Create a new account



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
customer_id = 56 # int | Customer's id
new_account_type = 56 # int | Account type (CHECKING, SAVINGS, LOAN)
from_account_id = 56 # int | Customer funds source account

try:
    # Create a new account
    api_response = api_instance.create_account1(customer_id, new_account_type, from_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_account1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 
 **new_account_type** | **int**| Account type (CHECKING, SAVINGS, LOAN) | 
 **from_account_id** | **int**| Customer funds source account | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deposit1**
> str deposit1(account_id, amount)

Deposit funds



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Customer funds target account
amount = 8.14 # float | Amount

try:
    # Deposit funds
    api_response = api_instance.deposit1(account_id, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->deposit1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Customer funds target account | 
 **amount** | **float**| Amount | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account1**
> Account get_account1(account_id)

Get Account by Id



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Account id

try:
    # Get Account by Id
    api_response = api_instance.get_account1(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Account id | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts1**
> list[Account] get_accounts1(customer_id)

Get Customer Accounts



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
customer_id = 56 # int | Customer's id

try:
    # Get Customer Accounts
    api_response = api_instance.get_accounts1(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_accounts1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 

### Return type

[**list[Account]**](Account.md)

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
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Account id

try:
    # Get the list of Transactions for the account
    api_response = api_instance.get_transactions1(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_transactions1: %s\n" % e)
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
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Account id
amount = 8.14 # float | Amount

try:
    # Create transactions by amount for account
    api_response = api_instance.get_transactions_by_amount1(account_id, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_transactions_by_amount1: %s\n" % e)
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
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Account id
month = 'month_example' # str | Month to use for the search range
type = 'type_example' # str | Transaction type (CREDIT, DEBIT)

try:
    # Fetch transactions by month and type for account
    api_response = api_instance.get_transactions_by_month_and_type1(account_id, month, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_transactions_by_month_and_type1: %s\n" % e)
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
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Account id
from_date = 'from_date_example' # str | Search starting date
to_date = 'to_date_example' # str | Search ending date

try:
    # Fetch transactions for date range for account
    api_response = api_instance.get_transactions_by_to_from_date1(account_id, from_date, to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_transactions_by_to_from_date1: %s\n" % e)
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
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Account id
on_date = 'on_date_example' # str | Search specific date

try:
    # Fetch transactions for a specific date for account
    api_response = api_instance.get_transactions_on_date1(account_id, on_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_transactions_on_date1: %s\n" % e)
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

# **transfer1**
> str transfer1(from_account_id, to_account_id, amount)

Transfer funds



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
from_account_id = 56 # int | Customer funds source account
to_account_id = 56 # int | Customer funds target account
amount = 8.14 # float | Amount

try:
    # Transfer funds
    api_response = api_instance.transfer1(from_account_id, to_account_id, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->transfer1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_account_id** | **int**| Customer funds source account | 
 **to_account_id** | **int**| Customer funds target account | 
 **amount** | **float**| Amount | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw1**
> str withdraw1(account_id, amount)

Withdraw funds



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
account_id = 56 # int | Customer funds source account
amount = 8.14 # float | Amount

try:
    # Withdraw funds
    api_response = api_instance.withdraw1(account_id, amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->withdraw1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| Customer funds source account | 
 **amount** | **float**| Amount | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

