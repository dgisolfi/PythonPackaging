#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Client 

Author(s)
---------

Daniel Gisolfi <Daniel.Gisolfi@ibm.com>
"""

import json
from typing import List

import requests

from coffee.utils.logger import Logger
from coffee.api.exceptions import *


class Client:
    def __init__(self, *args, **kwargs):
        self.host = kwargs.get("host", None)
        self.port = kwargs.get("port", 5984)
        self.base_url = f"http://{self.host}:{self.port}/api"

        self.logger = Logger().logger

        self.session = requests.session()

        self.session.headers.update(
            {"accept": "application/json", "content-type": "application/json"}
        )

    def __repr__(self):
        return f"<Coffee Client connected to Server: {self.base_url}>"

    def __del__(self):
        self.session.close()

    def _request(self, method, url, **kwargs) -> requests.Response:
        """Creates a request with the current session

        Parameters
        ----------
        method : str
            HTTP Method
        url : str
            url to request

        Returns
        -------
        Response
            response object

        Raises
        ------
        RequestError
            Request Failed
        """
        try:
            return self.session.request(method, url, **kwargs)
        except Exception as e:
            self.logger.debug(e)
            raise RequestError(f"Request to {self.host} failed: Error: {e}")

    def get(self, endpoint: str) -> dict:
        """Retrieves a document by its ID

        Parameters
        ----------
        endpoint : str
            the endpoint to preform a get request, example: /menu

        Returns
        -------
        dict
            Response Content

        Raises
        ------
        GetError
            The resource was not retrieved, an error occured
        ResourceDoesNotExist
            Could not find resource to delete
        """
        r = self._request("get", f"{self.base_url}/{endpoint}")

        if r.status_code == 200:
            self.logger.info(f"Retrieved resource from {endpoint}")
            return r.json()
        elif r.status_code == 404:
            raise ResourceDoesNotExist(json.loads(r.content.decode("utf-8")))
        else:
            raise GetError(json.loads(r.content.decode("utf-8")))

    def post(self, order: List[dict]) -> json:
        """Create a new order

        Parameters
        ----------
        order : List[dict]
            A list of drink orders

        Returns
        -------
        dict
            Response Content

        Raises
        ------
        PlaceOrderError
            Unable to create order
        """
        r = self._request("post", f"{self.base_url}/order", json=order)

        if r.status_code == 201:
            oid = r.json().get("oid", "ERROR")
            self.logger.info(f"Created order {oid}")
            return r.json()
        else:
            raise PostError(json.loads(r.content.decode("utf-8")))

    def delete(self, identifier, endpoint="order") -> dict:
        """Deletes a document given its ID

        Parameters
        ----------
        identifier : str
            Resource Identifier

        endpoint : str, optional
            resource to delete

        Returns
        -------
        dict
            Response Content
               
        Raises
        ------
        DeleteError
            The document was not deleted, an error occured
        ResourceDoesNotExist
            Could not find resource to delete
        """

        r = self._request("delete", f"{self.base_url}/{endpoint}/{identifier}")

        if r.status_code == 200:
            self.logger.info(f"Deleted {endpoint}: {identifier}")
            return r.json()
        elif r.status_code == 404:
            # self.logger()
            raise ResourceDoesNotExist(json.loads(r.content.decode("utf-8")))
        else:
            raise DeleteError(json.loads(r.content.decode("utf-8")))
