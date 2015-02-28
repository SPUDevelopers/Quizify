"""
Quizlet API Class
"""

#!/usr/bin/env python3

import sys
import json

import urllib.request
import urllib.parse

class Quizlet:

    client_id = 'p7jaJN9kEv'
    api_key = '4JRgAgZwm4jnekrPRk23pt'

    def make_definition_request(self, word):
        if word is None:
            return None

        request = 'https://api.quizlet.com/2.0/search/definitions?client_id='
        request += urllib.parse.quote(self.client_id)
        request += '&whitespace=1&q='
        request += urllib.parse.quote(word)
        request += '&limit=1'  # Limiting to 1 definition

        return request

    def query_definition(self, word):
        request = self.make_definition_request(word)
        response = urllib.request.urlopen(request)

        return self.parse_definition_json(str(response.read(), 'utf-8'))

    def parse_definition_json(self, data):
        json_data = json.loads(data)

        definition = json_data['official_definitions'][0]['definition']

        return definition

# https://api.quizlet.com/2.0/sets/415?client_id=p7jaJN9kEv&whitespace=1
# https://api.quizlet.com/2.0/search/definitions?client_id=p7jaJN9kEv&whitespace=1&q=testing&limit=1

if __name__ == '__main__':
    my_quiz = Quizlet()
    request = my_quiz.make_definition_request('transition')
    print(request)
    result = my_quiz.query_definition('transition')
    print(result)