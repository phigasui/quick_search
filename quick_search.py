#! /usr/bin/env python3

import webbrowser
import sys
import urllib.parse


engines = {
    'google': 'https://www.google.co.jp/#q=',
    'yahoo': 'http://search.yahoo.co.jp/search?p='
}


class quick_search():
    def __init__(self, queries, engine='google'):
        self.queries = queries
        self.engine = engine if engine in engines else 'google'

    def search(self):
        url = (engines[self.engine]
               + urllib.parse.quote_plus(' '.join(self.queries)))
        webbrowser.open(url)


if __name__ == '__main__':
    queries = sys.argv[1:]
    google = quick_search(queries)

    google.search()
