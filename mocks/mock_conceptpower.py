__author__ = 'diging_yogi'


class MockResponse:

    def __init__(self, xml_data, status_code, content):
            self.xml = xml_data
            self.status_code = status_code
            self.content = content

    def xml(self):
            return self.xml




def mocked_requests_get(*args, **kwargs):

     with open('search_sample', 'r') as myfile:
         data = myfile.read().replace('\n', '')


     return MockResponse('',200,data)

    # if args[0] == 0:
    #     with open('search_sample', 'r') as myfile:
    #             data=myfile.read().replace('\n', '')
    #     return MockResponse('',200,data)
    # else:
    #     return MockResponse('',200,'')
    #
    # return MockResponse({}, 404)