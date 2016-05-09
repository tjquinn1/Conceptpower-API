__author__ = 'diging_yogi'


import unittest

from requests.auth import HTTPBasicAuth
from conceptpower import classes
from httmock import with_httmock
from ..mocks import mock_conceptpower



class TestConceptpower(unittest.TestCase):

    @with_httmock(mock_conceptpower.create)
    def test_create(self):

        auth = HTTPBasicAuth('test','test')

        self.assertRaises(Exception, mymod.myfunc)
        results = classes.create()
        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('name' in results)
        self.assertEqual(results['name'], repo)

    @with_httmock
    def test_get(self):

