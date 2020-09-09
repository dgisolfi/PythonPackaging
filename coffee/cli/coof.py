#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Coof

A little easter egg :)

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi@ibm.com>

Usage
-----
    python3 -m tnt coof
"""

import click

from coffee.utils.logger import Logger


@click.command(name="coof", help="Shows a coof", hidden=True)
@click.help_option("-h", "--help")
@click.pass_context
def hiss(ctx, **kwargs):
    """ Generate example templates and models """
    # Initialize the logger
    logger = Logger().logger
    # combine the current context with sub command options
    ctx.obj.update(**kwargs)
    print("    (  )   (   )  )")
    print("     ) (   )  (  (")
    print("     ( )  (    ) )")
    print("     _____________")
    print("    <_____________> ___")
    print("    |             |/ _ \\")
    print("    |               | | |")
    print("    |               |_| |")
    print(" ___|             |\___/")
    print("/    \___________/    \\")
    print("\_____________________/")
    print("Have you had your coffee?")
