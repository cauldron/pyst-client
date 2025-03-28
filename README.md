# pyst-client

[![PyPI](https://img.shields.io/pypi/v/pyst-client.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/pyst-client.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/pyst-client)][pypi status]
[![License](https://img.shields.io/pypi/l/pyst-client)][pypi status]
[![Tests](https://github.com/cauldron/pyst-client/actions/workflows/python.yml/badge.svg)][tests]

[pypi status]: https://pypi.org/project/pyst-client/
[tests]: https://github.com/cauldron/pyst-client/actions?workflow=Tests

A Python client library for the PyST (Python Semantic Taxonomy) API.

## Overview

This client library provides a Python interface to interact with the PyST API, which is a Knowledge Organization System for Sustainability Assessment. It allows you to programmatically manage and query semantic taxonomies, concepts, and their relationships.

## Requirements

- Python 3.12+

## Installation

### From PyPI

```bash
pip install pyst-client
```

### From Source

```bash
git clone https://github.com/cauldron/pyst-client.git
cd pyst-client
pip install -e .
```

## Generating the Client

This client is [automatically generated](https://openapi-generator.tech/docs/usage) from an OpenAPI specification.
You can regenerate it using the following steps:

1. Install the OpenAPI Generator CLI:

   ```bash
   $ pip install openapi-generator-cli[jdk4py]
   ```

2. Generate the client using the existing configuration:

   ```bash
   $ openapi-generator-cli generate -i openapi.json -g python -o . -c generator-config.json
   ```

   The `openapi.json` file can be either:
   - A local file in the project root
   - A URL pointing to your PyST API's OpenAPI specification (e.g., `http://your-api/openapi.json`)

## Usage

Here's a basic example of how to use the client:

```python
import pyst_client
from pyst_client.rest import ApiException
from pprint import pprint

# Configure the client
configuration = pyst_client.Configuration(
    host = "http://localhost"  # Replace with your PyST server URL
)

# Create an API client
async with pyst_client.ApiClient(configuration) as api_client:
    # Create an instance of the Concept API
    concept_api = pyst_client.ConceptApi(api_client)

    try:
        # Create a new concept
        concept_create = pyst_client.ConceptCreate(
            # Add your concept details here
        )
        response = await concept_api.concept_create_concept_post(concept_create)
        print("Created concept:", response)
    except ApiException as e:
        print(f"Error creating concept: {e}")
```

## API Documentation

The client provides access to the following main API endpoints:

- **ConceptApi**: Manage concepts and their relationships
- **ConceptSchemeApi**: Handle concept schemes
- **ConceptAssociationApi**: Manage concept associations
- **CorrespondenceApi**: Handle concept correspondences

For detailed API documentation, see the [API Reference](docs/README.md).

## Development

### Setup Development Environment

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
pytest
```

### Code Style

This project follows PEP 8 guidelines. To check your code:

```bash
flake8
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConceptApi* | [**concept_create_concept_post**](docs/ConceptApi.md#concept_create_concept_post) | **POST** /concept/ | Create a &#x60;Concept&#x60; object
*ConceptApi* | [**concept_delete_concept_delete**](docs/ConceptApi.md#concept_delete_concept_delete) | **DELETE** /concept/ | Delete a &#x60;Concept&#x60; object
*ConceptApi* | [**concept_get_concept_get**](docs/ConceptApi.md#concept_get_concept_get) | **GET** /concept/ | Get a &#x60;Concept&#x60; object
*ConceptApi* | [**concept_search_concept_search_get**](docs/ConceptApi.md#concept_search_concept_search_get) | **GET** /concept/search/ | Search for &#x60;Concept&#x60; objects
*ConceptApi* | [**concept_suggest_concept_suggest_get**](docs/ConceptApi.md#concept_suggest_concept_suggest_get) | **GET** /concept/suggest/ | Suggestion search for &#x60;Concept&#x60; objects
*ConceptApi* | [**concept_update_concept_put**](docs/ConceptApi.md#concept_update_concept_put) | **PUT** /concept/ | Update a &#x60;Concept&#x60; object
*ConceptApi* | [**relationship_delete_relationships_delete**](docs/ConceptApi.md#relationship_delete_relationships_delete) | **DELETE** /relationships/ | Delete a list of &#x60;Concept&#x60; relationships
*ConceptApi* | [**relationships_create_relationships_post**](docs/ConceptApi.md#relationships_create_relationships_post) | **POST** /relationships/ | Create a list of &#x60;Concept&#x60; relationships
*ConceptApi* | [**relationships_get_relationships_get**](docs/ConceptApi.md#relationships_get_relationships_get) | **GET** /relationships/ | Get a list of &#x60;Concept&#x60; relationships
*ConceptAssociationApi* | [**association_create_association_post**](docs/ConceptAssociationApi.md#association_create_association_post) | **POST** /association/ | Create an &#x60;Association&#x60; object
*ConceptAssociationApi* | [**association_delete_association_delete**](docs/ConceptAssociationApi.md#association_delete_association_delete) | **DELETE** /association/ | Delete an &#x60;Association&#x60; object
*ConceptAssociationApi* | [**association_get_association_get**](docs/ConceptAssociationApi.md#association_get_association_get) | **GET** /association/ | Get an &#x60;Association&#x60; object
*ConceptSchemeApi* | [**concept_scheme_create_concept_scheme_post**](docs/ConceptSchemeApi.md#concept_scheme_create_concept_scheme_post) | **POST** /concept_scheme/ | Create a &#x60;ConceptScheme&#x60; object
*ConceptSchemeApi* | [**concept_scheme_delete_concept_scheme_delete**](docs/ConceptSchemeApi.md#concept_scheme_delete_concept_scheme_delete) | **DELETE** /concept_scheme/ | Delete a &#x60;ConceptScheme&#x60; object
*ConceptSchemeApi* | [**concept_scheme_get_concept_scheme_get**](docs/ConceptSchemeApi.md#concept_scheme_get_concept_scheme_get) | **GET** /concept_scheme/ | Get a &#x60;ConceptScheme&#x60; object
*ConceptSchemeApi* | [**concept_scheme_update_concept_scheme_put**](docs/ConceptSchemeApi.md#concept_scheme_update_concept_scheme_put) | **PUT** /concept_scheme/ | Update a &#x60;ConceptScheme&#x60; object
*CorrespondenceApi* | [**correspondence_create_correspondence_post**](docs/CorrespondenceApi.md#correspondence_create_correspondence_post) | **POST** /correspondence/ | Create a &#x60;Correspondence&#x60; object
*CorrespondenceApi* | [**correspondence_delete_correspondence_delete**](docs/CorrespondenceApi.md#correspondence_delete_correspondence_delete) | **DELETE** /correspondence/ | Delete a &#x60;Correspondence&#x60; object
*CorrespondenceApi* | [**correspondence_get_correspondence_get**](docs/CorrespondenceApi.md#correspondence_get_correspondence_get) | **GET** /correspondence/ | Get a &#x60;Correspondence&#x60; object
*CorrespondenceApi* | [**correspondence_update_correspondence_put**](docs/CorrespondenceApi.md#correspondence_update_correspondence_put) | **PUT** /correspondence/ | Update a &#x60;Correspondence&#x60; object
*CorrespondenceApi* | [**made_of_add_made_of_post**](docs/CorrespondenceApi.md#made_of_add_made_of_post) | **POST** /made_of/ | Add some &#x60;Correspondence&#x60; &#x60;madeOf&#x60; links
*CorrespondenceApi* | [**made_of_remove_made_of_delete**](docs/CorrespondenceApi.md#made_of_remove_made_of_delete) | **DELETE** /made_of/ | Remove some &#x60;Correspondence&#x60; &#x60;madeOf&#x60; links


## Documentation For Models

 - [AssociationInput](docs/AssociationInput.md)
 - [AssociationOutput](docs/AssociationOutput.md)
 - [Concept](docs/Concept.md)
 - [ConceptCreate](docs/ConceptCreate.md)
 - [ConceptSchemeInput](docs/ConceptSchemeInput.md)
 - [ConceptSchemeOutput](docs/ConceptSchemeOutput.md)
 - [ConceptUpdate](docs/ConceptUpdate.md)
 - [CorrespondenceInput](docs/CorrespondenceInput.md)
 - [CorrespondenceOutput](docs/CorrespondenceOutput.md)
 - [DateTime](docs/DateTime.md)
 - [DateTimeType](docs/DateTimeType.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [MadeOf](docs/MadeOf.md)
 - [MultilingualString](docs/MultilingualString.md)
 - [Node](docs/Node.md)
 - [NonLiteralNote](docs/NonLiteralNote.md)
 - [Notation](docs/Notation.md)
 - [RelationshipInput](docs/RelationshipInput.md)
 - [RelationshipOutput](docs/RelationshipOutput.md)
 - [SearchResult](docs/SearchResult.md)
 - [Status](docs/Status.md)
 - [StatusChoice](docs/StatusChoice.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [VersionString](docs/VersionString.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author
