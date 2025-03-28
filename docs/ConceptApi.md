# pyst_client.ConceptApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**concept_create_concept_post**](ConceptApi.md#concept_create_concept_post) | **POST** /concept/ | Create a &#x60;Concept&#x60; object
[**concept_delete_concept_delete**](ConceptApi.md#concept_delete_concept_delete) | **DELETE** /concept/ | Delete a &#x60;Concept&#x60; object
[**concept_get_concept_get**](ConceptApi.md#concept_get_concept_get) | **GET** /concept/ | Get a &#x60;Concept&#x60; object
[**concept_search_concept_search_get**](ConceptApi.md#concept_search_concept_search_get) | **GET** /concept/search/ | Search for &#x60;Concept&#x60; objects
[**concept_suggest_concept_suggest_get**](ConceptApi.md#concept_suggest_concept_suggest_get) | **GET** /concept/suggest/ | Suggestion search for &#x60;Concept&#x60; objects
[**concept_update_concept_put**](ConceptApi.md#concept_update_concept_put) | **PUT** /concept/ | Update a &#x60;Concept&#x60; object
[**relationship_delete_relationships_delete**](ConceptApi.md#relationship_delete_relationships_delete) | **DELETE** /relationships/ | Delete a list of &#x60;Concept&#x60; relationships
[**relationships_create_relationships_post**](ConceptApi.md#relationships_create_relationships_post) | **POST** /relationships/ | Create a list of &#x60;Concept&#x60; relationships
[**relationships_get_relationships_get**](ConceptApi.md#relationships_get_relationships_get) | **GET** /relationships/ | Get a list of &#x60;Concept&#x60; relationships


# **concept_create_concept_post**
> Concept concept_create_concept_post(concept_create, x_pyst_auth_token=x_pyst_auth_token)

Create a `Concept` object

### Example


```python
import pyst_client
from pyst_client.models.concept import Concept
from pyst_client.models.concept_create import ConceptCreate
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
    api_instance = pyst_client.ConceptApi(api_client)
    concept_create = pyst_client.ConceptCreate() # ConceptCreate | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Create a `Concept` object
        api_response = await api_instance.concept_create_concept_post(concept_create, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of ConceptApi->concept_create_concept_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->concept_create_concept_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_create** | [**ConceptCreate**](ConceptCreate.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**Concept**](Concept.md)

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

# **concept_delete_concept_delete**
> concept_delete_concept_delete(iri, x_pyst_auth_token=x_pyst_auth_token)

Delete a `Concept` object

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
    api_instance = pyst_client.ConceptApi(api_client)
    iri = 'iri_example' # str | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Delete a `Concept` object
        await api_instance.concept_delete_concept_delete(iri, x_pyst_auth_token=x_pyst_auth_token)
    except Exception as e:
        print("Exception when calling ConceptApi->concept_delete_concept_delete: %s\n" % e)
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

# **concept_get_concept_get**
> Concept concept_get_concept_get(iri)

Get a `Concept` object

### Example


```python
import pyst_client
from pyst_client.models.concept import Concept
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
    api_instance = pyst_client.ConceptApi(api_client)
    iri = 'iri_example' # str | 

    try:
        # Get a `Concept` object
        api_response = await api_instance.concept_get_concept_get(iri)
        print("The response of ConceptApi->concept_get_concept_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->concept_get_concept_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**|  | 

### Return type

[**Concept**](Concept.md)

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

# **concept_search_concept_search_get**
> List[SearchResult] concept_search_concept_search_get(query, language, semantic=semantic)

Search for `Concept` objects

### Example


```python
import pyst_client
from pyst_client.models.search_result import SearchResult
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
    api_instance = pyst_client.ConceptApi(api_client)
    query = 'query_example' # str | 
    language = 'language_example' # str | 
    semantic = True # bool |  (optional) (default to True)

    try:
        # Search for `Concept` objects
        api_response = await api_instance.concept_search_concept_search_get(query, language, semantic=semantic)
        print("The response of ConceptApi->concept_search_concept_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->concept_search_concept_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **language** | **str**|  | 
 **semantic** | **bool**|  | [optional] [default to True]

### Return type

[**List[SearchResult]**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**503** | Search engine not available |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **concept_suggest_concept_suggest_get**
> List[SearchResult] concept_suggest_concept_suggest_get(query, language)

Suggestion search for `Concept` objects

### Example


```python
import pyst_client
from pyst_client.models.search_result import SearchResult
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
    api_instance = pyst_client.ConceptApi(api_client)
    query = 'query_example' # str | 
    language = 'language_example' # str | 

    try:
        # Suggestion search for `Concept` objects
        api_response = await api_instance.concept_suggest_concept_suggest_get(query, language)
        print("The response of ConceptApi->concept_suggest_concept_suggest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->concept_suggest_concept_suggest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **language** | **str**|  | 

### Return type

[**List[SearchResult]**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**503** | Search engine not available |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **concept_update_concept_put**
> Concept concept_update_concept_put(concept_update, x_pyst_auth_token=x_pyst_auth_token)

Update a `Concept` object

### Example


```python
import pyst_client
from pyst_client.models.concept import Concept
from pyst_client.models.concept_update import ConceptUpdate
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
    api_instance = pyst_client.ConceptApi(api_client)
    concept_update = pyst_client.ConceptUpdate() # ConceptUpdate | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Update a `Concept` object
        api_response = await api_instance.concept_update_concept_put(concept_update, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of ConceptApi->concept_update_concept_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->concept_update_concept_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_update** | [**ConceptUpdate**](ConceptUpdate.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**Concept**](Concept.md)

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

# **relationship_delete_relationships_delete**
> object relationship_delete_relationships_delete(relationship_input, x_pyst_auth_token=x_pyst_auth_token)

Delete a list of `Concept` relationships

### Example


```python
import pyst_client
from pyst_client.models.relationship_input import RelationshipInput
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
    api_instance = pyst_client.ConceptApi(api_client)
    relationship_input = [pyst_client.RelationshipInput()] # List[RelationshipInput] | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Delete a list of `Concept` relationships
        api_response = await api_instance.relationship_delete_relationships_delete(relationship_input, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of ConceptApi->relationship_delete_relationships_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->relationship_delete_relationships_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship_input** | [**List[RelationshipInput]**](RelationshipInput.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

**object**

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

# **relationships_create_relationships_post**
> List[RelationshipOutput] relationships_create_relationships_post(relationship_input, x_pyst_auth_token=x_pyst_auth_token)

Create a list of `Concept` relationships

### Example


```python
import pyst_client
from pyst_client.models.relationship_input import RelationshipInput
from pyst_client.models.relationship_output import RelationshipOutput
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
    api_instance = pyst_client.ConceptApi(api_client)
    relationship_input = [pyst_client.RelationshipInput()] # List[RelationshipInput] | 
    x_pyst_auth_token = '' # str |  (optional) (default to '')

    try:
        # Create a list of `Concept` relationships
        api_response = await api_instance.relationships_create_relationships_post(relationship_input, x_pyst_auth_token=x_pyst_auth_token)
        print("The response of ConceptApi->relationships_create_relationships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->relationships_create_relationships_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relationship_input** | [**List[RelationshipInput]**](RelationshipInput.md)|  | 
 **x_pyst_auth_token** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**List[RelationshipOutput]**](RelationshipOutput.md)

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

# **relationships_get_relationships_get**
> List[RelationshipOutput] relationships_get_relationships_get(iri, source=source, target=target)

Get a list of `Concept` relationships

### Example


```python
import pyst_client
from pyst_client.models.relationship_output import RelationshipOutput
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
    api_instance = pyst_client.ConceptApi(api_client)
    iri = 'iri_example' # str | 
    source = True # bool |  (optional) (default to True)
    target = False # bool |  (optional) (default to False)

    try:
        # Get a list of `Concept` relationships
        api_response = await api_instance.relationships_get_relationships_get(iri, source=source, target=target)
        print("The response of ConceptApi->relationships_get_relationships_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConceptApi->relationships_get_relationships_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iri** | **str**|  | 
 **source** | **bool**|  | [optional] [default to True]
 **target** | **bool**|  | [optional] [default to False]

### Return type

[**List[RelationshipOutput]**](RelationshipOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

