# swagger_client.CustomersApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account1**](CustomersApi.md#create_account1) | **POST** /createAccount | Create a new account
[**get_accounts1**](CustomersApi.md#get_accounts1) | **GET** /customers/{customerId}/accounts | Get Customer Accounts
[**get_customer1**](CustomersApi.md#get_customer1) | **GET** /customers/{customerId} | Get Customer Details
[**get_positions1**](CustomersApi.md#get_positions1) | **GET** /customers/{customerId}/positions | Get Positions for Customer
[**update_customer1**](CustomersApi.md#update_customer1) | **POST** /customers/update/{customerId} | Update customer information


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
api_instance = swagger_client.CustomersApi()
customer_id = 56 # int | Customer's id
new_account_type = 56 # int | Account type (CHECKING, SAVINGS, LOAN)
from_account_id = 56 # int | Customer funds source account

try:
    # Create a new account
    api_response = api_instance.create_account1(customer_id, new_account_type, from_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_account1: %s\n" % e)
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
api_instance = swagger_client.CustomersApi()
customer_id = 56 # int | Customer's id

try:
    # Get Customer Accounts
    api_response = api_instance.get_accounts1(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_accounts1: %s\n" % e)
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

# **get_customer1**
> Customer get_customer1(customer_id)

Get Customer Details



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomersApi()
customer_id = 56 # int | Customer's id

try:
    # Get Customer Details
    api_response = api_instance.get_customer1(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_positions1**
> list[Position] get_positions1(customer_id)

Get Positions for Customer



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomersApi()
customer_id = 56 # int | Customer's id

try:
    # Get Positions for Customer
    api_response = api_instance.get_positions1(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_positions1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 

### Return type

[**list[Position]**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer1**
> str update_customer1(customer_id, first_name, last_name, street, city, state, zip_code, phone_number, ssn, username, password)

Update customer information



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomersApi()
customer_id = 56 # int | Customer's id
first_name = 'first_name_example' # str | Customer's given (first) name
last_name = 'last_name_example' # str | Customer's surname (last name)
street = 'street_example' # str | Street Address including bilding number and apartment (if any)
city = 'city_example' # str | City
state = 'state_example' # str | US state or Region name
zip_code = 'zip_code_example' # str | ZIP code or province id
phone_number = 'phone_number_example' # str | Contact Phone Number
ssn = 'ssn_example' # str | Social Security Number
username = 'username_example' # str | Customer's user name
password = 'password_example' # str | Customer's password

try:
    # Update customer information
    api_response = api_instance.update_customer1(customer_id, first_name, last_name, street, city, state, zip_code, phone_number, ssn, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_customer1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 
 **first_name** | **str**| Customer&#39;s given (first) name | 
 **last_name** | **str**| Customer&#39;s surname (last name) | 
 **street** | **str**| Street Address including bilding number and apartment (if any) | 
 **city** | **str**| City | 
 **state** | **str**| US state or Region name | 
 **zip_code** | **str**| ZIP code or province id | 
 **phone_number** | **str**| Contact Phone Number | 
 **ssn** | **str**| Social Security Number | 
 **username** | **str**| Customer&#39;s user name | 
 **password** | **str**| Customer&#39;s password | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

