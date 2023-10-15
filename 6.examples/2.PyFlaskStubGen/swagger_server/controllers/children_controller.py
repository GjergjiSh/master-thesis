import connexion
import six

from swagger_server.models.child import Child  # noqa: E501
from swagger_server import util


def children_cid_delete(cid):  # noqa: E501
    """Deletes the child with the provided id

     # noqa: E501

    :param cid: Child id
    :type cid: int

    :rtype: None
    """
    return 'do some magic!'


def children_cid_get(cid):  # noqa: E501
    """Returns the child with the provided id

     # noqa: E501

    :param cid: Child id
    :type cid: int

    :rtype: Child
    """
    return 'do some magic!'


def children_cid_put(cid):  # noqa: E501
    """Updates the child with the provided id

     # noqa: E501

    :param cid: Child id
    :type cid: int

    :rtype: Child
    """
    return 'do some magic!'


def children_get():  # noqa: E501
    """Returns all available children

     # noqa: E501


    :rtype: List[Child]
    """
    return 'do some magic!'


def children_post(body=None):  # noqa: E501
    """Adds a new child

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Child.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
