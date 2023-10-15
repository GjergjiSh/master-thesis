import connexion
import six

from swagger_server.models.parent import Parent  # noqa: E501
from swagger_server import util


def get_parent(pid):  # noqa: E501
    """Returns the parent with the provided id

     # noqa: E501

    :param pid: Parent id
    :type pid: int

    :rtype: Parent
    """
    return 'do some magic!'
