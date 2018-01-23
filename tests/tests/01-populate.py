#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import requests
import time
from urllib.parse import urlencode, quote_plus
import json
import os

import lorem

class Populate(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Populate, self).__init__(*args, **kwargs)

        if 'API_BASE_URL' in os.environ:
            self.base_url = os.environ.get('API_BASE_URL')
        else:
            self.base_url = "http://localhost:9040/"

        self.base_url_api = self.base_url + "v1/"
        self.base_url_api_pages = self.base_url_api + "pages"

    def test_00_ping_to_server(self):
        reply = requests.get(
            url=self.base_url_api
        )
        self.assertEqual(reply.status_code, 200)
        data = reply.json()
        self.assertTrue('_links' in data)
        self.assertTrue('child' in data['_links'])
        self.assertEqual(len(data['_links']['child']), 1)

    def test_05_db_is_empty(self):
        reply = requests.get(
            url=self.base_url_api_pages
        )
        self.assertEqual(reply.status_code, 200)
        reply_object = reply.json()
        self.assertEqual(len(reply_object['_items']), 0)

    def test_10_create_10_test_pages(self):
        for sequential_number in range(0,10):
            page_payload = {}
            page_payload['title'] = "Test page {}".format(sequential_number)
            content = "Test page {} content\n\n".format(sequential_number)
            for lorem_index in range(0,10):
                content = content + lorem.text() + "\n\n"

            page_payload['content'] = content
            page_payload['authors'] = [0,1,2,3,4,5]
            page_payload['language'] = 'en'

            search_filter = {"title":"Test page {}".format(sequential_number)}
            search_filter_query = urlencode({"where":json.dumps(search_filter)})

            search_reply = requests.get(
                url=self.base_url_api_pages + "?" + search_filter_query
            )
            self.assertEqual(search_reply.status_code, 200)

            search_object = search_reply.json()

            self.assertEqual(len(search_object['_items']), 0)

            create_reply = requests.post(
                url=self.base_url_api_pages,
                json=page_payload
            )
            self.assertEqual(create_reply.status_code, 201)
            create_object = create_reply.json()

            get_reply = requests.get(
                url=self.base_url_api + create_object['_links']['self']['href']
            )
            self.assertEqual(get_reply.status_code, 200)
            get_object = get_reply.json()

            self.assertEqual(get_object['_deleted'],False)
            self.assertEqual(get_object['_version'],1)
            self.assertEqual(get_object['_latest_version'],1)

            for key in page_payload:
                self.assertEqual(get_object[key],page_payload[key])

if __name__ == '__main__':
    unittest.main()
