__author__ = 'diging_yogi'

import unittest

from requests.auth import HTTPBasicAuth
from httmock import with_httmock
import mock
import mocks.mock_conceptpower
import conceptpower


class TestConceptpower(unittest.TestCase):


    """
    testing the "search" method when there is no concept for
    the lemma we are searching
    """
    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_search)
    def test_search_no_concepts(self,mock_search):
        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.search('Bradshaw', 0)
        self.assertIsInstance(val, list)
        self.assertEqual(len(val), 0)


    """
    testing the "search" method when there are concepts for
    the lemma we are searching
    """
    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_search)
    def test_search(self,mock_search):
        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.search('Bradshaw', 1)
        self.assertIsInstance(val, list)
        self.assertEqual(len(val), 1)
        self.assertEqual(len(val[0]),15)
