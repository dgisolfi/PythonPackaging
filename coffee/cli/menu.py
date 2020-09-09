#!/usr/bin/env python3

"""Menu

Shows the coffee menu

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


@click.command(name="menu", help="Shows the menu")
@click.help_option("-h", "--help")
@click.pass_context
def menu(ctx, **kwargs):
    """ Show the menu """
    # Initialize the logger
    logger = Logger().logger
    # combine the current context with sub command options
    ctx.obj.update(**kwargs)

    store = jsonToDict(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "api/store.json")
    )

    client = Client(**store)
    menu = client.get("menu")

    # print(list(menu[0].keys()))
    print("{:<15} {:<30} {:<30} {:<10}".format("name", "sizes", "prices", "calories"))
    for item in menu:
        name = item["name"]
        size = ", ".join(item["size"])
        price = ", ".join((map(str, item["price"])))
        calories = item["calories"]
        print("{:<15} {:<30} {:<30} {:<10}".format(name, size, price, calories))
