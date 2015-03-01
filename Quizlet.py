"""
Quizlet API Class
"""

#!/usr/bin/env python3

import sys
import json

import urllib.request
import urllib.parse

import http.client


class Quizlet:

    client_id = 'p7jaJN9kEv'
    api_key = '4JRgAgZwm4jnekrPRk23pt'

    def __init__(self):
        self.auth_token = 'be9b45472195218d08593f46c56ef658e0d5a071'

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

        try:
            definition = json_data['official_definitions'][0]['definition']
        except:
            definition = "No definition found for this word."

        return definition

    # AUTHORIZATION
    def authorize(self, secret_code):
        #request = '/authorize?response_type=code&client_id='
        #request += urllib.parse.quote(self.client_id)
        #request += '&scope=write_set'
        #request += '&state=RANDOM_STRING'

        #hc = http.client.HTTPConnection('https://quizlet.com')
        #test = hc.request('GET', request)

        #auth_response = urllib.request.urlopen(request)
        #parsed_resp = urllib.parse.urlparse(auth_response.getcode())
        #secret_code = parsed_resp[2]

        # Get auth token
        values = urllib.parse.urlencode({'grant_type': 'authorization_code', 'code':secret_code, 'redirect_uri': 'wangi.cs.spu.edu'})
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Basic ' + 'cDdqYUpOOWtFdjo0SlJnQWdad200am5la3JQUmsyM3B0'}

        conn = http.client.HTTPSConnection('api.quizlet.com')
        conn.request('POST', '/oauth/token', values, headers)
        response = conn.getresponse()

        data = str(response.read(), 'utf-8')
        print(data)

        # Parse auth token
        json_data = json.loads(data)
        self.auth_token = json_data['access_token']
        print(self.auth_token)

    def add_flashcard(self, word):


# https://api.quizlet.com/2.0/sets/415?client_id=p7jaJN9kEv&whitespace=1
# https://api.quizlet.com/2.0/search/definitions?client_id=p7jaJN9kEv&whitespace=1&q=testing&limit=1

# https://quizlet.com/authorize?response_type=code&client_id=p7jaJN9kEv&scope=read&state=RANDOM_STRING

if __name__ == '__main__':
    my_quiz = Quizlet()
    my_quiz.authorize('548c1ddefe2eaf9e47b48e17566380cda8e7a6e4')