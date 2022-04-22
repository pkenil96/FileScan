import connexion

from swagger_server.models.sms_object import SMSObject  # noqa: E501
from swagger_server import util


def send_sms(body=None):  # noqa: E501
    """sends SMS to the user

    sends SMS to the user # noqa: E501

    :param body: SMS Object to be sent
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SMSObject.from_dict(connexion.request.get_json())  # noqa: E501
        messageBody = body.get('messageBody', '')
        destination = body.get('destination', '')
        print('Initiating process to send message to ' + destination)
        return None
    return 'Something went wrong'

    

