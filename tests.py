__author__ = 'diging_yogi'

import unittest

from requests.auth import HTTPBasicAuth
from httmock import with_httmock
import mock
import mocks.mock_conceptpower
import conceptpower


class TestConceptpower(unittest.TestCase):
    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_search)
    def test_search_no_concepts(self, mock_search):
        """
        testing the "search" method when there is no concept for
        the lemma we are searching
        """

        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.search('abcdef')
        self.assertIsInstance(val, list)
        self.assertEqual(len(val), 0)


    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_search)
    def test_search(self, mock_search):
        """
        testing the "search" method when there are concepts for
        the lemma we are searching
        """

        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.search('Bradshaw')
        self.assertIsInstance(val, list)
        self.assertEqual(len(val), 1)
        self.assertEqual(len(val[0]),15)


    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_get)
    def test_get_no_concept(self, mock_get):
        """
        testing the "get" method when there is no concept for
        the Concept URI we are searching
        :param mock_get:
        :return:
        """

        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.get('http://www.digitalhps.org/concepts/abcdefg')
        self.assertIsInstance(val,dict)
        self.assertEqual(len(val),0)

    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_get)
    def test_get(self, mock_get):
        """
        testing the "get" method when there is no concept for
        the Concept URI we are searching
        :param mock_get:
        :return:
        """

        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.get('http://www.digitalhps.org/concepts/CON536b243d-3c71-4a5c-ab79-3c7f12765b3f')
        self.assertIsInstance(val,dict)
        self.assertEqual(len(val),15)

    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_get_type)
    def test_get_type_no_concept(self, mock_get_type):
        """
        testing the "get_type" method when there is no concept for
        the Concept URI we are searching
        :param mock_get_type:
        :return:
        """

        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.get_type('http://www.digitalhps.org/types/TYPE_abadf')
        self.assertIsInstance(val,dict)
        self.assertEqual(len(val),0)

    @mock.patch('requests.get', side_effect=mocks.mock_conceptpower.mocked_requests_get_type)
    def test_get_type_concept(self, mock_get_type):
        """
        testing the "get_type" method when there is concept for
        the Concept URI we are searching
        :param mock_get_type:
        :return:
        """

        conceptPower = conceptpower.Conceptpower()
        val = conceptPower.get_type('http://www.digitalhps.org/types/TYPE_986a7cc9-c0c1-4720-b344-853f08c136ab')
        self.assertIsInstance(val,dict)
        self.assertEqual(len(val),5)

if __name__ == '__main__':
    unittest.main()
