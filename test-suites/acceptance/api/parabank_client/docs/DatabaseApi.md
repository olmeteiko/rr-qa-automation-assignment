# swagger_client.DatabaseApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clean_db1**](DatabaseApi.md#clean_db1) | **POST** /cleanDB | Clean the Database
[**initialize_db1**](DatabaseApi.md#initialize_db1) | **POST** /initializeDB | Initialize the Database


# **clean_db1**
> clean_db1()

Clean the Database



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatabaseApi()

try:
    # Clean the Database
    api_instance.clean_db1()
except ApiException as e:
    print("Exception when calling DatabaseApi->clean_db1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_db1**
> initialize_db1()

Initialize the Database



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DatabaseApi()

try:
    # Initialize the Database
    api_instance.initialize_db1()
except ApiException as e:
    print("Exception when calling DatabaseApi->initialize_db1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

