# swagger_client.PositionsApi

All URIs are relative to *http://localhost/parabank/services/bank*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buy_position1**](PositionsApi.md#buy_position1) | **POST** /customers/{customerId}/buyPosition | Buy a Position
[**get_position1**](PositionsApi.md#get_position1) | **GET** /positions/{positionId} | Get Position by id
[**get_position_history1**](PositionsApi.md#get_position_history1) | **GET** /positions/{positionId}/{startDate}/{endDate} | Get Position history by id within a date range
[**get_positions1**](PositionsApi.md#get_positions1) | **GET** /customers/{customerId}/positions | Get Positions for Customer
[**sell_position1**](PositionsApi.md#sell_position1) | **POST** /customers/{customerId}/sellPosition | Sell a Position


# **buy_position1**
> list[Position] buy_position1(customer_id, account_id, name, symbol, shares, price_per_share)

Buy a Position



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
customer_id = 56 # int | Customer's id
account_id = 56 # int | Customer funds source account
name = 'name_example' # str | Instrument's Name
symbol = 'symbol_example' # str | Instrument's exchange symbol
shares = 56 # int | number of shares
price_per_share = 8.14 # float | Price of each share

try:
    # Buy a Position
    api_response = api_instance.buy_position1(customer_id, account_id, name, symbol, shares, price_per_share)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->buy_position1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 
 **account_id** | **int**| Customer funds source account | 
 **name** | **str**| Instrument&#39;s Name | 
 **symbol** | **str**| Instrument&#39;s exchange symbol | 
 **shares** | **int**| number of shares | 
 **price_per_share** | **float**| Price of each share | 

### Return type

[**list[Position]**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position1**
> Position get_position1(position_id)

Get Position by id



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
position_id = 56 # int | Unique identifier for the position

try:
    # Get Position by id
    api_response = api_instance.get_position1(position_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->get_position1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **int**| Unique identifier for the position | 

### Return type

[**Position**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position_history1**
> list[HistoryPoint] get_position_history1(position_id, start_date, end_date)

Get Position history by id within a date range



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
position_id = 56 # int | Unique identifier for the position
start_date = 'start_date_example' # str | Search starting date
end_date = 'end_date_example' # str | Search ending date

try:
    # Get Position history by id within a date range
    api_response = api_instance.get_position_history1(position_id, start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->get_position_history1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **int**| Unique identifier for the position | 
 **start_date** | **str**| Search starting date | 
 **end_date** | **str**| Search ending date | 

### Return type

[**list[HistoryPoint]**](HistoryPoint.md)

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
api_instance = swagger_client.PositionsApi()
customer_id = 56 # int | Customer's id

try:
    # Get Positions for Customer
    api_response = api_instance.get_positions1(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->get_positions1: %s\n" % e)
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

# **sell_position1**
> list[Position] sell_position1(customer_id, account_id, position_id, shares, price_per_share)

Sell a Position



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PositionsApi()
customer_id = 56 # int | Customer's id
account_id = 56 # int | Customer funds target account
position_id = 56 # int | Unique identifier for the position
shares = 56 # int | number of shares
price_per_share = 8.14 # float | Price of each share

try:
    # Sell a Position
    api_response = api_instance.sell_position1(customer_id, account_id, position_id, shares, price_per_share)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PositionsApi->sell_position1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer&#39;s id | 
 **account_id** | **int**| Customer funds target account | 
 **position_id** | **int**| Unique identifier for the position | 
 **shares** | **int**| number of shares | 
 **price_per_share** | **float**| Price of each share | 

### Return type

[**list[Position]**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

