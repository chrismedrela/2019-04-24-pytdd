import unittest
from unittest import mock

from webtest import TestApp

import webapp


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.client = TestApp(webapp.app)

    def test_webapp(self):
        resp = self.client.get('/')
        self.assertIn('Home Page', resp)

    @mock.patch('webapp.calc')
    def test_adding_two_numbers(self, calc_mock):
        calc_mock.add.return_value = 120
        args = [
            ('first', '50'), 
            ('second', '70'),
        ]
        resp = self.client.post('/', args)
        self.assertIn('120', resp)
        calc_mock.add.assert_called_once_with(50, 70)


if __name__ == "__main__":
    unittest.main()