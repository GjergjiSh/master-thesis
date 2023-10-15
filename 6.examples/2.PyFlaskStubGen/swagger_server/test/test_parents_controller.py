# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.parent import Parent  # noqa: E501
from swagger_server.test import BaseTestCase


class TestParentsController(BaseTestCase):
    """ParentsController integration test stubs"""

    def test_get_parent(self):
        """Test case for get_parent

        Returns the parent with the provided id
        """
        response = self.client.open(
            '/GJERGJISHKURTI/Family/1/parents/{pid}'.format(pid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
