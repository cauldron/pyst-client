# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pyst_client.api.correspondence_api import CorrespondenceApi


class TestCorrespondenceApi(unittest.IsolatedAsyncioTestCase):
    """CorrespondenceApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = CorrespondenceApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_correspondence_create_correspondence_post(self) -> None:
        """Test case for correspondence_create_correspondence_post

        Create a `Correspondence` object
        """
        pass

    async def test_correspondence_delete_correspondence_delete(self) -> None:
        """Test case for correspondence_delete_correspondence_delete

        Delete a `Correspondence` object
        """
        pass

    async def test_correspondence_get_correspondence_get(self) -> None:
        """Test case for correspondence_get_correspondence_get

        Get a `Correspondence` object
        """
        pass

    async def test_correspondence_update_correspondence_put(self) -> None:
        """Test case for correspondence_update_correspondence_put

        Update a `Correspondence` object
        """
        pass

    async def test_made_of_add_made_of_post(self) -> None:
        """Test case for made_of_add_made_of_post

        Add some `Correspondence` `madeOf` links
        """
        pass

    async def test_made_of_remove_made_of_delete(self) -> None:
        """Test case for made_of_remove_made_of_delete

        Remove some `Correspondence` `madeOf` links
        """
        pass


if __name__ == '__main__':
    unittest.main()
