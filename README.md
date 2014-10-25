Conceptpower API
================
A very simple library for querying a [Conceptpower](http://conceptpower.sourceforge.net/)
REST API.

Installation
------------
The ``conceptpower-api`` package is [available via PyPI](https://pypi.python.org/pypi?name=conceptpower-api&version=1.0&:action=display). 

```bash
$ pip install conceptpower-api
```

Usage
-----
Search for a Concept.

```python
>>> import conceptpower as cp
>>> cp.search('Bradshaw')
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
    ]
```

Get a Concept by URI.

```python
>>> import conceptpower as cp
>>> cp.get('http://www.digitalhps.org/concepts/CON536b243d-3c71-4a5c-ab79-3c7f12765b3f')
    {'conceptList': 'Persons',
     'description': 'A professor at the Cambridge Botany School',
     'id': 'http://www.digitalhps.org/concepts/CON536b243d-3c71-4a5c-ab79-3c7f12765b3f',
     'lemma': 'Sir Harry Godwin',
     'pos': 'noun',
     'type': 'E21 Person',
     'type_id': '986a7cc9-c0c1-4720-b344-853f08c136ab',
     'type_uri': 'http://www.digitalhps.org/types/TYPE_986a7cc9-c0c1-4720-b344-853f08c136ab'}
```

Set ``namespace`` and ``endpoint`` by passing them as keyword arguments...

```python
>>> cp.search('Bradshaw', endpoint='http://cp.myhost.com/rest/', 
...                       namespace='{http://mynamspace/}')
```

...or by defining them in a subclass.

```python
>>> from conceptpower import Conceptpower
>>> class CustomConceptpower(Conceptpower):
...     endpoint = 'http://cp.myhost.com/rest/'
...     namespace = '{http://mynamspace/}'
>>> cp = CustomConceptpower()
>>> cp.search('Bradshaw')
```

License
-------
Tethne is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Tethne is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
[GNU General Public License](http://www.gnu.org/licenses/) for more details.

![alt text](http://www.gnu.org/graphics/gplv3-127x51.png "GNU GPL 3")
