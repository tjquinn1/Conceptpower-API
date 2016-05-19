__author__ = 'diging_yogi'
import os

sample_data = '<conceptpowerReply xmlns:digitalHPS="http://www.digitalhps.org/">' \
              '<digitalHPS:conceptEntry><digitalHPS:id concept_id="CONe5b55803-1ef6-4abe-b81c-1493e97421df" ' \
              'concept_uri="http://www.digitalhps.org/concepts/CONe5b55803-1ef6-4abe-b81c-1493e97421df">' \
              'http://www.digitalhps.org/concepts/CONe5b55803-1ef6-4abe-b81c-1493e97421df</digitalHPS:id>' \
              '<digitalHPS:lemma>Margaret E. Bradshaw</digitalHPS:lemma><digitalHPS:pos>noun</digitalHPS:pos>' \
              '<digitalHPS:description>Botanist at the University of Exeter</digitalHPS:description>' \
              '<digitalHPS:conceptList>Persons</digitalHPS:conceptList>' \
              '<digitalHPS:creator_id>deryc.painter</digitalHPS:creator_id>' \
              '<digitalHPS:equal_to></digitalHPS:equal_to>' \
              '<digitalHPS:modified_by>erick@Thu Jul 24 09:59:24 MST 2014</digitalHPS:modified_by>' \
              '<digitalHPS:similar_to></digitalHPS:similar_to><digitalHPS:synonym_ids></digitalHPS:synonym_ids>' \
              '<digitalHPS:type type_id="986a7cc9-c0c1-4720-b344-853f08c136ab" ' \
              'type_uri="http://www.digitalhps.org/types/TYPE_986a7cc9-c0c1-4720-b344-853f08c136ab">E21 Person' \
              '</digitalHPS:type><digitalHPS:deleted>false</digitalHPS:deleted><digitalHPS:wordnet_id>' \
              '</digitalHPS:wordnet_id></digitalHPS:conceptEntry></conceptpowerReply>'

class MockResponse:

    def __init__(self, xml_data, status_code, content):
            self.xml = xml_data
            self.status_code = status_code
            self.content = content

    def xml(self):
            return self.xml


def mocked_requests_search(*args, **kwargs):

     empty_data = '<conceptpowerReply xmlns:digitalHPS="http://www.digitalhps.org/"></conceptpowerReply>'

     if args[0][-1] == '0':
        return MockResponse('', 200, empty_data)
     else:
        return MockResponse('', 200, sample_data)

