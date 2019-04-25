import unittest

import mock

from webapp import home


class HomeViewTest(unittest.TestCase):
    @mock.patch('webapp.request')
    def test_get_request(self, request_mock):
        request_mock.method = 'GET'

        html = home()

        self.assertIn('<form', html)

    @mock.patch('webapp.request')
    def test_post_request(self, request_mock):
        request_mock.method = 'POST'
        request_mock.form = {'number': '42'}

        html = home()

        self.assertIn('42+1 = 43', html)


if __name__ == "__main__":
    unittest.main()
