#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Exceptions 

Author(s)
---------

Daniel Gisolfi <Daniel.Gisolfi@ibm.com>
"""


class RequestError(Exception):
    pass


class GetError(Exception):
    pass


class PostError(Exception):
    pass


class DeleteError(Exception):
    pass


class ResourceDoesNotExist(Exception):
    pass
