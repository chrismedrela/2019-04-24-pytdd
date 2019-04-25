import os.path
import unittest

# try:
#     from unittest import mock
# except ImportError:
#     try:
#         import mock  # pip install mock
#     except ImportError as e:
#         e.message += "mock library is required on Python 2. Install with 'pip install mock'"
#         raise
from unittest import mock

import my_module
from my_module import my_remove


class NoMockingTestCase(unittest.TestCase):
    def test_provided_extension_should_be_used(self):
        filename = 'file.md'
        open(filename, 'w').close()
        self.assertTrue(os.path.isfile(filename))
        my_remove(filename)
        self.assertFalse(os.path.isfile(filename))

    def test_when_extension_is_missing_then_use_default_one(self):
        filename = 'file.txt'
        open(filename, 'w').close()
        self.assertTrue(os.path.isfile(filename))
        my_remove('file')
        self.assertFalse(os.path.isfile(filename))


class PatchingTestCase(unittest.TestCase):
    @mock.patch('my_module.os')
    def test_provided_extension_should_be_used(self, os_mock):
        my_remove('file.md')
        os_mock.remove.assert_called_once_with('file.md')

    @mock.patch('my_module.os')
    def test_when_extension_is_missing_then_use_default_one(self, os_mock):
        my_remove('file')
        os_mock.remove.assert_called_once_with('file.txt')


@mock.patch('my_module.os')
class ClassPatchingTestCase(unittest.TestCase):
    def test_provided_extension_should_be_used(self, os_mock):
        my_remove('file.md')
        os_mock.remove.assert_called_once_with('file.md')

    def test_when_extension_is_missing_then_use_default_one(self, os_mock):
        my_remove('file')
        os_mock.remove.assert_called_once_with('file.txt')


class PatchingInSetupTestCase(unittest.TestCase):
    def setUp(self):
        self.os_patcher = mock.patch('my_module.os')
        self.os_mock = self.os_patcher.start()
        self.addCleanup(self.os_patcher.stop)

    def test_provided_extension_should_be_used(self):
        my_remove('file.md')
        self.os_mock.remove.assert_called_once_with('file.md')

    def test_when_extension_is_missing_then_use_default_one(self):
        my_remove('file')
        self.os_mock.remove.assert_called_once_with('file.txt')


class PatchAsContextManager(unittest.TestCase):
    def test_provided_extension_should_be_used(self):
        with mock.patch('my_module.os') as os_mock:
            my_remove('file.md')
            os_mock.remove.assert_called_once_with('file.md')


class ManualPatching(unittest.TestCase):
    def setUp(self):
        self.os_mock = mock.Mock()
        self.real_os = my_module.os
        my_module.os = self.os_mock
        self.addCleanup(self.cleanup_os_mock)

    def cleanup_os_mock(self):
        my_module.os = self.real_os

    def test_provided_extension_should_be_used(self):
        my_remove('file.md')
        self.os_mock.remove.assert_called_once_with('file.md')


if __name__ == "__main__":
    unittest.main()
