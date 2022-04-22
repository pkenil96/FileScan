# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.sms_object import SMSObject  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_send_sms(self):
        """Test case for send_sms

        sends SMS to the user
        """
        body = SMSObject()
        response = self.client.open(
            '/pkenil96/PhoneMessager/1.0.0/send/sms',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
