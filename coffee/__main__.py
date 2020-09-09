#!/usr/bin/env python3

"""Main Entry point for the package

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>

Usage
-----
    python3 -m template
"""

from coffee.cli import cli, addCmds


def main():
    """ Wrapper for CLI """
    addCmds()
    cli()


if __name__ == "__main__":
    main()
