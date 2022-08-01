# swagger_client.JMSApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shutdown_jms_listener1**](JMSApi.md#shutdown_jms_listener1) | **POST** /shutdownJmsListener | Stop JMS Listener
[**startup_jms_listener1**](JMSApi.md#startup_jms_listener1) | **POST** /startupJmsListener | Start JMS Listener


# **shutdown_jms_listener1**
> shutdown_jms_listener1()

Stop JMS Listener



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JMSApi()

try:
    # Stop JMS Listener
    api_instance.shutdown_jms_listener1()
except ApiException as e:
    print("Exception when calling JMSApi->shutdown_jms_listener1: %s\n" % e)
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

# **startup_jms_listener1**
> startup_jms_listener1()

Start JMS Listener



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JMSApi()

try:
    # Start JMS Listener
    api_instance.startup_jms_listener1()
except ApiException as e:
    print("Exception when calling JMSApi->startup_jms_listener1: %s\n" % e)
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

