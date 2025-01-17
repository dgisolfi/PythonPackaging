# coding: utf-8

from __future__ import absolute_import

from typing import Dict, List  # noqa: F401
from datetime import date, datetime  # noqa: F401

from swagger_server import util
from swagger_server.models.drink import Drink  # noqa: F401,E501
from swagger_server.models.base_model_ import Model


class Order(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """Order - a model defined in Swagger

        """
        self.swagger_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "Order":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The order of this Order.  # noqa: E501
        :rtype: Order
        """
        return util.deserialize_model(dikt, cls)
