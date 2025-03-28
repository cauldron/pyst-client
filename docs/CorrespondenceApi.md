# pyst_client.CorrespondenceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**correspondence_create_correspondence_post**](CorrespondenceApi.md#correspondence_create_correspondence_post) | **POST** /correspondence/ | Create a &#x60;Correspondence&#x60; object
[**correspondence_delete_correspondence_delete**](CorrespondenceApi.md#correspondence_delete_correspondence_delete) | **DELETE** /correspondence/ | Delete a &#x60;Correspondence&#x60; object
[**correspondence_get_correspondence_get**](CorrespondenceApi.md#correspondence_get_correspondence_get) | **GET** /correspondence/ | Get a &#x60;Correspondence&#x60; object
[**correspondence_update_correspondence_put**](CorrespondenceApi.md#correspondence_update_correspondence_put) | **PUT** /correspondence/ | Update a &#x60;Correspondence&#x60; object
[**made_of_add_made_of_post**](CorrespondenceApi.md#made_of_add_made_of_post) | **POST** /made_of/ | Add some &#x60;Correspondence&#x60; &#x60;madeOf&#x60; links
[**made_of_remove_made_of_delete**](CorrespondenceApi.md#made_of_remove_made_of_delete) | **DELETE** /made_of/ | Remove some &#x60;Correspondence&#x60; &#x60;madeOf&#x60; links


# **correspondence_create_correspondence_post**
> CorrespondenceOutput correspondence_create_correspondence_post(correspondence_input, x_pyst_auth_token=x_pyst_auth_token)

Create a `Correspondence` object

### Example


```python
import pyst_client
from pyst_client.models.correspondence_input import CorrespondenceInput
from pyst_client.models.correspondence_output import CorrespondenceOutput
from pyst_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyst_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyst_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyst_client.CorrespondenceApi(api_client)
    correspondence_input = pyst_client.CorrespondenceInput() # CorrespondenceInput | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Create a `Correspondence` object
        api_response = await api_instance.correspondence_create_correspondence_post(correspondence_input, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of CorrespondenceApi->correspondence_create_correspondence_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrespondenceApi->correspondence_create_correspondence_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correspondence_input** | [**CorrespondenceInput**](CorrespondenceInput.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CorrespondenceOutput**](CorrespondenceOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**409** | Resource already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correspondence_delete_correspondence_delete**
> correspondence_delete_correspondence_delete(iri, x_pyst_auth_token=x_pyst_auth_token)

Delete a `Correspondence` object

### Example


```python
import pyst_client
from pyst_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyst_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyst_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyst_client.CorrespondenceApi(api_client)
    iri = 'iri_example' # str | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Delete a `Correspondence` object
        await api_instance.correspondence_delete_correspondence_delete(iri, x_pyst_auth_token=x_pyst_auth_token)
    except Exception as e:
        print("Exception when calling CorrespondenceApi->correspondence_delete_correspondence_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correspondence_get_correspondence_get**
> CorrespondenceOutput correspondence_get_correspondence_get(iri)

Get a `Correspondence` object

### Example


```python
import pyst_client
from pyst_client.models.correspondence_output import CorrespondenceOutput
from pyst_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyst_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyst_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyst_client.CorrespondenceApi(api_client)
    iri = 'iri_example' # str | 

    try:
        # Get a `Correspondence` object
        api_response = await api_instance.correspondence_get_correspondence_get(iri)
        print("The response of CorrespondenceApi->correspondence_get_correspondence_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrespondenceApi->correspondence_get_correspondence_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**|  | 

### Return type

[**CorrespondenceOutput**](CorrespondenceOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correspondence_update_correspondence_put**
> CorrespondenceOutput correspondence_update_correspondence_put(correspondence_input, x_pyst_auth_token=x_pyst_auth_token)

Update a `Correspondence` object

### Example


```python
import pyst_client
from pyst_client.models.correspondence_input import CorrespondenceInput
from pyst_client.models.correspondence_output import CorrespondenceOutput
from pyst_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyst_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyst_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyst_client.CorrespondenceApi(api_client)
    correspondence_input = pyst_client.CorrespondenceInput() # CorrespondenceInput | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Update a `Correspondence` object
        api_response = await api_instance.correspondence_update_correspondence_put(correspondence_input, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of CorrespondenceApi->correspondence_update_correspondence_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrespondenceApi->correspondence_update_correspondence_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correspondence_input** | [**CorrespondenceInput**](CorrespondenceInput.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CorrespondenceOutput**](CorrespondenceOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **made_of_add_made_of_post**
> CorrespondenceOutput made_of_add_made_of_post(made_of, x_pyst_auth_token=x_pyst_auth_token)

Add some `Correspondence` `madeOf` links

### Example


```python
import pyst_client
from pyst_client.models.correspondence_output import CorrespondenceOutput
from pyst_client.models.made_of import MadeOf
from pyst_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyst_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyst_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyst_client.CorrespondenceApi(api_client)
    made_of = pyst_client.MadeOf() # MadeOf | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Add some `Correspondence` `madeOf` links
        api_response = await api_instance.made_of_add_made_of_post(made_of, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of CorrespondenceApi->made_of_add_made_of_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrespondenceApi->made_of_add_made_of_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **made_of** | [**MadeOf**](MadeOf.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CorrespondenceOutput**](CorrespondenceOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **made_of_remove_made_of_delete**
> CorrespondenceOutput made_of_remove_made_of_delete(made_of, x_pyst_auth_token=x_pyst_auth_token)

Remove some `Correspondence` `madeOf` links

### Example


```python
import pyst_client
from pyst_client.models.correspondence_output import CorrespondenceOutput
from pyst_client.models.made_of import MadeOf
from pyst_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pyst_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with pyst_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyst_client.CorrespondenceApi(api_client)
    made_of = pyst_client.MadeOf() # MadeOf | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Remove some `Correspondence` `madeOf` links
        api_response = await api_instance.made_of_remove_made_of_delete(made_of, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of CorrespondenceApi->made_of_remove_made_of_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CorrespondenceApi->made_of_remove_made_of_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **made_of** | [**MadeOf**](MadeOf.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**CorrespondenceOutput**](CorrespondenceOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

