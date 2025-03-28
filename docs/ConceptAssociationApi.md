# pyst_client.ConceptAssociationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**association_create_association_post**](ConceptAssociationApi.md#association_create_association_post) | **POST** /association/ | Create an &#x60;Association&#x60; object
[**association_delete_association_delete**](ConceptAssociationApi.md#association_delete_association_delete) | **DELETE** /association/ | Delete an &#x60;Association&#x60; object
[**association_get_association_get**](ConceptAssociationApi.md#association_get_association_get) | **GET** /association/ | Get an &#x60;Association&#x60; object


# **association_create_association_post**
> AssociationOutput association_create_association_post(association_input, x_pyst_auth_token=x_pyst_auth_token)

Create an `Association` object

### Example


```python
import pyst_client
from pyst_client.models.association_input import AssociationInput
from pyst_client.models.association_output import AssociationOutput
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
    api_instance = pyst_client.ConceptAssociationApi(api_client)
    association_input = pyst_client.AssociationInput() # AssociationInput | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Create an `Association` object
        api_response = await api_instance.association_create_association_post(association_input, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of ConceptAssociationApi->association_create_association_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptAssociationApi->association_create_association_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_input** | [**AssociationInput**](AssociationInput.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**AssociationOutput**](AssociationOutput.md)

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

# **association_delete_association_delete**
> association_delete_association_delete(iri, x_pyst_auth_token=x_pyst_auth_token)

Delete an `Association` object

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
    api_instance = pyst_client.ConceptAssociationApi(api_client)
    iri = 'iri_example' # str | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Delete an `Association` object
        await api_instance.association_delete_association_delete(iri, x_pyst_auth_token=x_pyst_auth_token)
    except Exception as e:
        print("Exception when calling ConceptAssociationApi->association_delete_association_delete: %s\n" % e)
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

# **association_get_association_get**
> AssociationOutput association_get_association_get(iri)

Get an `Association` object

### Example


```python
import pyst_client
from pyst_client.models.association_output import AssociationOutput
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
    api_instance = pyst_client.ConceptAssociationApi(api_client)
    iri = 'iri_example' # str | 

    try:
        # Get an `Association` object
        api_response = await api_instance.association_get_association_get(iri)
        print("The response of ConceptAssociationApi->association_get_association_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptAssociationApi->association_get_association_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**|  | 

### Return type

[**AssociationOutput**](AssociationOutput.md)

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

