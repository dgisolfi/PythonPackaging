import json

import six

import connexion
from swagger_server import util
from swagger_server.models.item import Item  # noqa: E501
from swagger_server.models.menu import Menu  # noqa: E501

# DISCLAMIER: This is quick code used for a demo.

menu = [
    {
        "name": "Americano",
        "size": ["small", "medium", "large"],
        "price": [3.00, 4.00, 5.00],
        "calories": 100,
    },
    {
        "name": "Espresso",
        "size": ["single", "double"],
        "price": [2.00, 3.00],
        "calories": 100,
    },
    {
        "name": "Cold Brew",
        "size": ["small", "medium", "large"],
        "price": [12.00, 15.00, 18.00],
        "calories": 3,
    },
    {
        "name": "Cappuccino",
        "size": ["small", "medium", "large"],
        "price": [4.00, 5.00, 6.00],
        "calories": 400,
    },
]


def get_menu():  # noqa: E501
    """Returns all possible drinks

     # noqa: E501


    :rtype: List[Menu]
    """
    return menu


def get_menu_item(name):  # noqa: E501
    """Returns a drink specified by name

     # noqa: E501

    :param name: 
    :type name: str

    :rtype: Item
    """
    for item in menu:
        if item["name"].lower().strip() == name.lower().strip():
            return item

    return "Drink could not be found", 404
