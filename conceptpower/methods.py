"""Methods for resolving concepts in Conceptpower (http://chps.asu.edu)."""

import urllib2
import xml.etree.ElementTree as ET
from pprint import pprint

host = "http://chps.asu.edu/conceptpower/rest/"

class conceptpower:
    def __init__(self):
        pass
    
    def search (self, query, pos):
        """
        Searches for a noun, and returns a list of dictionaries with concept details.
        
        Keyword arguments:
        query -- a search term
        pos -- part of speach: Noun, Verb, etc.
        
        Example:
        >>> pprint (cp.search("Bradshaw", "Noun"))                                      
        [{'conceptList': 'Persons',
          'description': 'Plant ecologist',
          'id': 'http://www.digitalhps.org/concepts/066efc74-8710-4a1f-9111-3a27d880438e',
          'lemma': 'Anthony David Bradshaw (1926-2008)',
          'pos': 'noun',
          'type': 'E21 Person'},
         {'conceptList': 'Persons',
          'description': 'Botanist at the University of Exeter',
          'id': 'http://www.digitalhps.org/concepts/CONe5b55803-1ef6-4abe-b81c-1493e97421df',
          'lemma': 'Margaret E. Bradshaw',
          'pos': 'noun',
          'type': 'E21 Person'},
         {'conceptList': 'Publications',
          'description': 'Bradshaw, Anthony David. 1965. "The evolutionary significance of phenotypic plasticity in plants." Advances in Genetics 13: 115-155.',
          'id': 'http://www.digitalhps.org/concepts/CON76832db2-7abb-4c77-b08e-239017b6a585',
          'lemma': 'Bradshaw 1965',
          'pos': 'noun',
          'type': 'E28 Conceptual Object '},
         {'conceptList': 'Phenotypic Plasticity',
          'description': None,
          'id': 'http://www.digitalhps.org/concepts/72ec32b4-2a20-4d26-ab8f-a173f067542d',
          'lemma': 'Anthony D. Bradshaw',
          'pos': 'noun',
          'type': None}]
        """
        
        query = query.replace(" ", "%20")
        response = urllib2.urlopen(host+"ConceptLookup/"+query+"/"+pos).read()
        root = ET.fromstring(response)
        data = []
        if len(root) > 0:
            for node in root:
                if node.tag == '{http://www.digitalhps.org/}conceptEntry':
                    datum = {}
                    for snode in node:
                        datum[snode.tag.replace('{http://www.digitalhps.org/}', '')] = snode.text
                    data.append(datum)
        return data

    def get (self, uri):
        """Retrieves a dictionary with data about the provided CP URI.
        
        Keyword arguments:
        uri -- the full Conceptpower URI, or an ID, as string. For example: http://www.digitalhps.org/CON7971a85a-49e1-424d-84e6-697262bd2510
        
        Example:
        >>> pprint (cp.get("http://www.digitalhps.org/concepts/CON536b243d-3c71-4a5c-ab79-3c7f12765b3f"))
        {'conceptList': 'Persons',
         'description': 'A professor at the Cambridge Botany School',
         'id': 'http://www.digitalhps.org/concepts/CON536b243d-3c71-4a5c-ab79-3c7f12765b3f',
         'lemma': 'Sir Harry Godwin',
         'pos': 'noun',
         'type': 'E21 Person',
         'type_id': '986a7cc9-c0c1-4720-b344-853f08c136ab',
         'type_uri': 'http://www.digitalhps.org/types/TYPE_986a7cc9-c0c1-4720-b344-853f08c136ab'}
        """

        response = urllib2.urlopen(host+"Concept?id="+uri).read()
        root = ET.fromstring(response)
        data = {}
        if len(root) > 0:
            for node in root:
                if node.tag == '{http://www.digitalhps.org/}conceptEntry':
                    for snode in node:
                        data[snode.tag.replace('{http://www.digitalhps.org/}', '')] = snode.text
                        if snode.tag == '{http://www.digitalhps.org/}type':
                            data['type_id'] = snode.get('type_id')
                            data['type_uri'] = snode.get('type_uri')
        return data