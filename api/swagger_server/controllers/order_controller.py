import six

import connexion
from swagger_server import util
from swagger_server.models.drink import Drink  # noqa: E501
from swagger_server.models.order import Order  # noqa: E501

orders = {}


def create_order(body=None):  # noqa: E501
    """Creates a order for a list of drinks

     # noqa: E501

    :param body: a order
    :type body: list | bytes

    :rtype: object
    """
    msg = "error creating order"
    ret_code = 400
    if connexion.request.is_json:
        oid = 0 if len(orders) == 0 else list(orders.keys())[-1] + 1
        orders[oid] = connexion.request.get_json()
        msg = {"status": f"order created", "oid": oid}
        ret_code = 201

    return msg, ret_code


def del_order(oid):  # noqa: E501
    """Deletes an existing order by order id

     # noqa: E501

    :param oid: 
    :type oid: str

    :rtype: Order
    """
    oid = int(oid)
    msg = "error deleting order"
    ret_code = 400
    if oid in orders:
        del orders[oid]
        msg = {"status": f"order deleted", "oid": oid}
        ret_code = 200
    else:
        msg = f"Order: {oid} could not be found"
        ret_code = 404

    return msg, ret_code


def get_order(oid):  # noqa: E501
    """Gets an existing order by order id

     # noqa: E501

    :param oid: 
    :type oid: str

    :rtype: Order
    """
    oid = int(oid)
    msg = "error retrieving order"
    ret_code = 400
    if oid in orders:
        msg = {"status": f"order retrieved", "order": orders[oid], "oid": oid}
        ret_code = 200
    else:
        msg = f"Order: {oid} could not be found"
        ret_code = 404

    return msg, ret_code
