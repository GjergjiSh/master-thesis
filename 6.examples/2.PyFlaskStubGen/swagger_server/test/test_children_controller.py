# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.child import Child  # noqa: E501
from swagger_server.test import BaseTestCase


class TestChildrenController(BaseTestCase):
    """ChildrenController integration test stubs"""

    def test_children_cid_delete(self):
        """Test case for children_cid_delete

        Deletes the child with the provided id
        """
        response = self.client.open(
            '/GJERGJISHKURTI/Family/1/children/{cid}'.format(cid=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_children_cid_get(self):
        """Test case for children_cid_get

        Returns the child with the provided id
        """
        response = self.client.open(
            '/GJERGJISHKURTI/Family/1/children/{cid}'.format(cid=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_children_cid_put(self):
        """Test case for children_cid_put

        Updates the child with the provided id
        """
        response = self.client.open(
            '/GJERGJISHKURTI/Family/1/children/{cid}'.format(cid=56),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_children_get(self):
        """Test case for children_get

        Returns all available children
        """
        response = self.client.open(
            '/GJERGJISHKURTI/Family/1/children/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_children_post(self):
        """Test case for children_post

        Adds a new child
        """
        body = Child()
        response = self.client.open(
            '/GJERGJISHKURTI/Family/1/children/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
