#!/usr/bin/env python
import unittest
from web.server import server

class TestHello(unittest.TestCase):

    def setUp(self):
        server.testing = True
        self.server = server.test_client()

    def test_health_status(self):
        rv = self.server.get('/health')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'App is healthy\n')


if __name__ == '__main__':
    unittest.main()
