__author__ = 'Isaac Wang'


import urllib.request
import urllib.parse

import re
import xml.etree.ElementTree as ET


class WordDefiner:
    API_KEY = '564b7dde-f126-44cc-b784-5c7b99d2a384'

    def __init__(self):
        pass

    def query_definition(self, word):
        if word is None:
            return ''

        request = self.make_request(word, WordDefiner.API_KEY)
        response = urllib.request.urlopen(request)

        return self.parse_definition(str(response.read(), 'utf-8'))

    def make_request(self, word, key):
        if word is None:
            return ''

        request = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/'
        request += urllib.parse.quote(word.strip()) # Change special characters into escape sequences
        request += '?key='
        request += urllib.parse.quote(key.strip())

        return request

    def parse_definition(self, xml):
        definition_list = []

        root = ET.fromstring(xml)

        # Find suggestions
        if root.find('suggestion'):
            return None  # Could not find word

        for entry in root.findall('entry'):
            for definition in entry.findall('def'):
                for dt in entry.findall('dt'):
                    text = dt.text
                    # PARSE AND PUSH THE DEFINITION

        if len(definition_list) == 0:
            return None

        return definition_list


if __name__ == '__main__':
    my_definer = WordDefiner()
    request = my_definer.make_request('transition', my_definer.API_KEY)
    print(request)

    response = my_definer.query_definition('transition')
    print(response)
