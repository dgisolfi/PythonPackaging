#!/usr/bin/env python3

"""Store

Sets the store to order from

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi@ibm.com>

Usage
-----
    python3 -m coffee store
"""

import os

import click

from coffee.utils.io import saveJSON
from coffee.utils.logger import Logger


@click.command(name="store", help="Sets the store to order from")
@click.help_option("-h", "--help")
@click.pass_context
def store(ctx, **kwargs):
    """ Show the menu """
    # Initialize the logger
    logger = Logger().logger
    # combine the current context with sub command options
    ctx.obj.update(**kwargs)

    location = {}

    location["host"] = input("What is the store host? ☕️ ")
    location["port"] = input("What is the store port? ☕️ ")

    logger.info("Saving store details")
    saveJSON(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "api/store.json"),
        location,
    )
