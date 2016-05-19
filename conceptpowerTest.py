__author__ = 'diging_yogi'

__author__ = 'diging_yogi'


import unittest

from requests.auth import HTTPBasicAuth
from httmock import with_httmock
import mock
import mocks.mock_conceptpower
import conceptpower


class TestConceptpower(unittest.TestCase):

    # @with_httmock(mock_conceptpower.create)
    # def test_create(self):
    #
    #     auth = HTTPBasicAuth('test','test')
    #
    #     self.assertRaises(Exception, mymod.myfunc)
    #     results = classes.create()
    #     self.assertNotEqual(results, None)
    #     self.assertIsInstance(results, dict)
    #     self.assertTrue('name' in results)
    #     self.assertEqual(results['name'], repo)

    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_get)
    def test_search(self,mock_get):
        conceptPower = conceptpower.Conceptpower()
        #conceptPower.search()
        val = conceptPower.search(0,'Bradshaw')
        self.assertEqual(len(val),4)
