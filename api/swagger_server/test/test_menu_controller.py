# coding: utf-8

from __future__ import absolute_import

from six import BytesIO

from flask import json
from swagger_server.test import BaseTestCase
from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.menu import Menu  # noqa: E501


class TestMenuController(BaseTestCase):
    """MenuController integration test stubs"""

    def test_get_menu(self):
        """Test case for get_menu

        Returns all possible drinks
        """
        response = self.client.open("/menu", method="GET")
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_menu_item(self):
        """Test case for get_menu_item

        Returns a drink specified by name
        """
        response = self.client.open(
            "/menu/{name}".format(name="name_example"), method="GET"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
