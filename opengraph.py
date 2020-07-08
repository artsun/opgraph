# encoding: utf-8

import re
from urllib import request
from bs4 import BeautifulSoup


class OpenGraph(dict):
    """
    за основу взята библиотека opengraph_py3
    https://pypi.org/project/opengraph_py3/
    https://github.com/erikriver/opengraph
    """
    def __init__(self, url: str, headers: dict):
        dict.__init__(self)
        self._fetch(url, headers)

    def __setattr__(self, name: str, val: str):
        self[name] = val

    def __getattr__(self, name: str):
        return self[name]

    def _fetch(self, url: str, headers: dict) -> None:
        try:
            raw = request.Request(url=url, headers=headers)
        except ValueError:  # unknown url type
            return self.update({'error': 'incorrect url'})
        try:
            raw = request.urlopen(raw)
        except request.URLError:  # https://
            return self.update({'error': 'incorrect url'})
        html = raw.read()
        return self._parse(html)

    def _parse(self, html: bytes) -> None:
        doc = BeautifulSoup(html, features="html.parser")
        ogs = doc.html.head.findAll(property=re.compile(r'^og'))
        for og in ogs:
            if og.has_attr(u'content'):
                self[og[u'property'][3:]] = og[u'content']
