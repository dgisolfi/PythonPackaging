#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""CLI 

Author(s)
---------

Daniel Gisolfi <Daniel.Gisolfi@ibm.com>

Usage
-----
    python3 -m coffee
"""

import os
import sys
import importlib.util

import click

from coffee.__version__ import __title__, __version__
from coffee.utils.logger import Logger


@click.group()
# -h, --help
@click.help_option("-h", "--help")

# --version
@click.version_option(
    version=__version__,
    prog_name=__title__,
    message="You are using version %(version)s of %(prog)s",
)

# -v, --verbose
@click.option(
    "-v",
    "--verbose",
    required=False,
    is_flag=True,
    default=False,
    help="Set logging level to debug for both regular and file logging.",
)
@click.pass_context
def cli(ctx, **kwargs):
    """ Coffee
    Orders yummy beverages from a server

    Has Coof powers
    \f

    The cli for the Coffee API.
    """
    # create a object in the current context
    ctx.obj = kwargs

    # Initialize the logger
    Logger(verbose=ctx.obj["verbose"],).logger


def addCmds():
    """ 
    Gets all modules in the cli directory, 
    imports them and adds any commands it finds to click
    """
    excludes = ["__init__.py", "cmds.py"]

    # When a module is loaded from a file in Python, __file__ is set
    # to its path. So we can use this to get the dir path of all the commands
    cli_dir = os.path.dirname(__file__)
    for module_name in os.listdir(cli_dir):
        if module_name not in excludes:
            module_path = os.path.join(cli_dir, module_name)
            
            # Now we import the source file directly
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            for attr in dir(module):
                cmd = getattr(module, attr)
                if callable(cmd) and type(cmd) is click.core.Command:
                    cli.add_command(cmd)
