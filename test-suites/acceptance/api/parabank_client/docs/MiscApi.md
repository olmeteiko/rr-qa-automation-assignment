# swagger_client.MiscApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login1**](MiscApi.md#login1) | **GET** /login/{username}/{password} | Login (john/demo)
[**set_parameter1**](MiscApi.md#set_parameter1) | **POST** /setParameter/{name}/{value} | Set Parameters


# **login1**
> Customer login1(username, password)

Login (john/demo)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MiscApi()
username = 'username_example' # str | Customer's user name
password = 'password_example' # str | Customer's password

try:
    # Login (john/demo)
    api_response = api_instance.login1(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->login1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Customer&#39;s user name | 
 **password** | **str**| Customer&#39;s password | 

### Return type

[**Customer**](Customer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parameter1**
> set_parameter1(name, value)

Set Parameters



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MiscApi()
name = 'name_example' # str | Parameter Name
value = 'value_example' # str | Parameter Value

try:
    # Set Parameters
    api_instance.set_parameter1(name, value)
except ApiException as e:
    print("Exception when calling MiscApi->set_parameter1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Parameter Name | 
 **value** | **str**| Parameter Value | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

