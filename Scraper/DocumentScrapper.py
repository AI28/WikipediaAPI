from bs4 import BeautifulSoup

from Scraper.DocumentGetter import DocumentGetter


class DocumentScrapper:
    _document_getter = None
    _document = None
    _parser = None

    def __init__(self, url):

        try:
            self._document_getter = DocumentGetter(url)
        except Exception as e:
            print(str(e))
            return

        self._document = self._document_getter.get_document()
        self._parser = BeautifulSoup(self._document, "html.parser")

    def scrap_document(self):
        return


class ListOfCountriesScrapper(DocumentScrapper):
    __elements = None

    def __init__(self, url):
        super().__init__(url)

    def scrap_document(self):
        aux = self._parser.find_all('a')
        self.__elements = [item.attrs["href"] for item in aux
                           if "title" in item.attrs
                           and item.attrs["href"].split('/')[2] == item.attrs["title"]
                           and item.attrs["title"] == item.string]

    def get_elements(self):
        if self.__elements is None:
            raise Exception("Exception. Unitialized elements list. Please call scrapDocument first.")

        return self.__elements


class CountryDataScrapper(DocumentScrapper):
    __country_card = None

    def __init__(self, url):
        super().__init__(url)

    def scrap_document(self):

        self.__country_card = self._parser.find('table', class_="infobox geography vcard")

    def get_country_card(self):

        if self.__country_card is None:
           self.scrap_document()

        return self.__country_card
