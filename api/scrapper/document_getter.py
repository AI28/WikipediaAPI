import requests
import re


class DocumentGetter:
    _url = None

    def __init__(self, url):

        validation_regex = re.compile("^https://en.wikipedia.org(.)*")

        if validation_regex.match(url):
            self._url = url
        else:
            raise Exception("Exception. Please enter a Wikipedia domain url.")

    def get_document(self):

        if self._url is None:
            raise Exception("Exception. Please initialise the url first.")

        r = requests.get(self._url)
        return r.text

    def get_url(self):

        if self._url is None:
            raise Exception("Exception. The url is uninitialised.")

        return self._url
