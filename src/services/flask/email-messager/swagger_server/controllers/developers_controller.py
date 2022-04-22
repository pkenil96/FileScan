import connexion
import six

from swagger_server.models.email_object import EmailObject  # noqa: E501
from swagger_server import util


def send_email(body=None):  # noqa: E501
    """sends email to the user

    sends email to the user # noqa: E501

    :param body: Email Object to be sent
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = EmailObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
