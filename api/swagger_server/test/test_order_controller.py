# coding: utf-8

from __future__ import absolute_import

from six import BytesIO

from flask import json
from swagger_server.test import BaseTestCase
from swagger_server.models.drink import Drink  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501


class TestOrderController(BaseTestCase):
    """OrderController integration test stubs"""

    def test_create_order(self):
        """Test case for create_order

        Creates a order for a list of drinks
        """
        body = [Drink()]
        response = self.client.open(
            "/order",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_del_order(self):
        """Test case for del_order

        Deletes an existing order by order id
        """
        response = self.client.open(
            "/order/{oid}".format(oid="oid_example"), method="DELETE"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_order(self):
        """Test case for get_order

        Gets an existing order by order id
        """
        response = self.client.open(
            "/order/{oid}".format(oid="oid_example"), method="GET"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
