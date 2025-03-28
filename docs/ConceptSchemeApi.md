# pyst_client.ConceptSchemeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**concept_scheme_create_concept_scheme_post**](ConceptSchemeApi.md#concept_scheme_create_concept_scheme_post) | **POST** /concept_scheme/ | Create a &#x60;ConceptScheme&#x60; object
[**concept_scheme_delete_concept_scheme_delete**](ConceptSchemeApi.md#concept_scheme_delete_concept_scheme_delete) | **DELETE** /concept_scheme/ | Delete a &#x60;ConceptScheme&#x60; object
[**concept_scheme_get_concept_scheme_get**](ConceptSchemeApi.md#concept_scheme_get_concept_scheme_get) | **GET** /concept_scheme/ | Get a &#x60;ConceptScheme&#x60; object
[**concept_scheme_update_concept_scheme_put**](ConceptSchemeApi.md#concept_scheme_update_concept_scheme_put) | **PUT** /concept_scheme/ | Update a &#x60;ConceptScheme&#x60; object


# **concept_scheme_create_concept_scheme_post**
> ConceptSchemeOutput concept_scheme_create_concept_scheme_post(concept_scheme_input, responses=responses, x_pyst_auth_token=x_pyst_auth_token)

Create a `ConceptScheme` object

### Example


```python
import pyst_client
from pyst_client.models.concept_scheme_input import ConceptSchemeInput
from pyst_client.models.concept_scheme_output import ConceptSchemeOutput
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
    api_instance = pyst_client.ConceptSchemeApi(api_client)
    concept_scheme_input = pyst_client.ConceptSchemeInput() # ConceptSchemeInput | 
    responses = None # object |  (optional)
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Create a `ConceptScheme` object
        api_response = await api_instance.concept_scheme_create_concept_scheme_post(concept_scheme_input, responses=responses, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of ConceptSchemeApi->concept_scheme_create_concept_scheme_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptSchemeApi->concept_scheme_create_concept_scheme_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_scheme_input** | [**ConceptSchemeInput**](ConceptSchemeInput.md)|  | 
 **responses** | [**object**](.md)|  | [optional] 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**ConceptSchemeOutput**](ConceptSchemeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **concept_scheme_delete_concept_scheme_delete**
> concept_scheme_delete_concept_scheme_delete(iri, x_pyst_auth_token=x_pyst_auth_token)

Delete a `ConceptScheme` object

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
    api_instance = pyst_client.ConceptSchemeApi(api_client)
    iri = 'iri_example' # str | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Delete a `ConceptScheme` object
        await api_instance.concept_scheme_delete_concept_scheme_delete(iri, x_pyst_auth_token=x_pyst_auth_token)
    except Exception as e:
        print("Exception when calling ConceptSchemeApi->concept_scheme_delete_concept_scheme_delete: %s\n" % e)
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

# **concept_scheme_get_concept_scheme_get**
> ConceptSchemeOutput concept_scheme_get_concept_scheme_get(iri)

Get a `ConceptScheme` object

### Example


```python
import pyst_client
from pyst_client.models.concept_scheme_output import ConceptSchemeOutput
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
    api_instance = pyst_client.ConceptSchemeApi(api_client)
    iri = 'iri_example' # str | 

    try:
        # Get a `ConceptScheme` object
        api_response = await api_instance.concept_scheme_get_concept_scheme_get(iri)
        print("The response of ConceptSchemeApi->concept_scheme_get_concept_scheme_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptSchemeApi->concept_scheme_get_concept_scheme_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**|  | 

### Return type

[**ConceptSchemeOutput**](ConceptSchemeOutput.md)

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

# **concept_scheme_update_concept_scheme_put**
> ConceptSchemeOutput concept_scheme_update_concept_scheme_put(concept_scheme_input, responses=responses, x_pyst_auth_token=x_pyst_auth_token)

Update a `ConceptScheme` object

### Example


```python
import pyst_client
from pyst_client.models.concept_scheme_input import ConceptSchemeInput
from pyst_client.models.concept_scheme_output import ConceptSchemeOutput
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
    api_instance = pyst_client.ConceptSchemeApi(api_client)
    concept_scheme_input = pyst_client.ConceptSchemeInput() # ConceptSchemeInput | 
    responses = None # object |  (optional)
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Update a `ConceptScheme` object
        api_response = await api_instance.concept_scheme_update_concept_scheme_put(concept_scheme_input, responses=responses, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of ConceptSchemeApi->concept_scheme_update_concept_scheme_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptSchemeApi->concept_scheme_update_concept_scheme_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_scheme_input** | [**ConceptSchemeInput**](ConceptSchemeInput.md)|  | 
 **responses** | [**object**](.md)|  | [optional] 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**ConceptSchemeOutput**](ConceptSchemeOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

