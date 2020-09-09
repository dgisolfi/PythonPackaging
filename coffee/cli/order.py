#!/usr/bin/env python3

"""Order

Places an order

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi@ibm.com>

Usage
-----
    python3 -m coffee menu
"""

import os

import click

from coffee.utils.io import jsonToDict
from coffee.api.client import Client
from coffee.utils.logger import Logger


@click.command(name="order", help="Order a drink")
@click.help_option("-h", "--help")
@click.pass_context
def order(ctx, **kwargs):
    """ Order a drink """
    # Initialize the logger
    logger = Logger().logger
    # combine the current context with sub command options
    ctx.obj.update(**kwargs)

    store = jsonToDict(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "api/store.json")
    )

    client = Client(**store)
    menu = client.get("menu")
    drinks = [d["name"].lower().strip() for d in menu]
    order = {}

    order["name"] = input("What drink would you like? ")
    if order["name"].lower().strip() not in drinks:
        Logger().error(
            f"'{order['name']}' is not a valid drink. Run the menu command to see valid options.",
            1,
        )

    order["size"] = input("What size should it be? ")
    for item in menu:
        if item["name"].lower().strip() == order["name"]:
            if order["size"].lower().strip() not in item["size"]:
                Logger().error(
                    f"'{order['size']}' is not a valid size. Run the menu command to see valid options.",
                    1,
                )

    order["iced"] = input("Do you want it iced? True|False ")
    if order["iced"] not in ["True", "False"]:
        Logger().error(
            f"'{order['iced']}' is not a valid answer. Please provide either True or False.",
            1,
        )
    else:
        order["iced"] = bool(order["iced"])

    logger.info("Sending order to server.")
    client.post([order])
