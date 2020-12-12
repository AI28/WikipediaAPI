import re

from bs4 import BeautifulSoup

from api.scrapper.document_getter import DocumentGetter


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

    def __scrap_document(self):
        aux = self._parser.find_all('a')
        self.__elements = [item.attrs["href"] for item in aux
                           if "title" in item.attrs
                           and item.attrs["href"].split('/')[2] == item.attrs["title"]
                           and item.attrs["title"] == item.string]

    def get_elements(self):
        if self.__elements is None:
            self.__scrap_document()

        return self.__elements


class CountryDataScrapper(DocumentScrapper):
    __country_card = None

    def __init__(self, url):
        super().__init__(url)
        self.scrap_document()

    def scrap_document(self):

        self.__country_card = self._parser.find('table', class_="infobox geography vcard")

    def get_country_name(self):

        """return super()._document_getter.get_url().split('/')[-1]"""
        if self.__country_card is None:
            self.scrap_document()

        aux = self.__country_card.find(class_="country-name")

        if aux is None:
            return aux

        return self.__country_card.find(class_="country-name").text

    def get_country_capital(self):

        if self.__country_card is None:
            return None

        t = self.get_country_card().find(text="Capital")

        if t is None:
            return None

        return t.find_parent().find_next_sibling().find("a").text

    def get_country_population(self):

        if self.__country_card is None:
            return 0

        t = self.get_country_card().find(text="Population")

        if t is None:
            return 0

        milions_re = re.compile("[1-9]\d{0,2}(,\d{3})*")

        aux = t.find_all_next(text=milions_re)[1]
        result = int(re.search(milions_re, str(aux.string))[0].replace(",", ''))

        if result < 100:
            return result * 1000000

        return result

    def get_country_language(self):

        if self.__country_card is None:
            self.scrap_document()

        t = set(self.get_country_card().find_all(title=re.compile("language$")))

        return list(filter(lambda x: re.match("language", x) is None, map(lambda x: x.text, t)))

    def get_country_government(self):
        if self.__country_card is None:
            self.scrap_document()

        t = self.__country_card.find(text="Government")

        if t is None:
            return None

        t1 = t.find_parent().find_parent().find_next_sibling("td")

        if t1 is None:
            return None

        return list(map(lambda x: x.text, t1.find_all("a")))

    def get_country_area(self):

        if self.__country_card is None:
            self.scrap_document()

        milions_re = re.compile("[1-9]\d{0,2}((,|\.)\d{3})*")

        area_element = self.__country_card.find(
            text=re.compile("Area")).find_parent().find_parent().find_parent().find_next_sibling()

        if area_element is None:
            return -1
        elif area_element.find("td") is None:
            return -1

        match = re.match(milions_re, area_element.find("td").text)

        if match is None:
            return -1
        elif match.group(0) is None:
            return -1

        return int(match.group(0).replace(",", ""))

    def get_neighbours(self):

        if self.__country_card is None:
            self.scrap_document()

        temp = list(map(lambda x: x.find_next_siblings(),
                        self._parser.find_all(string=re.compile("(bordered|surrounded|shares|borders)"))))
        temp2 = [item.text for sublist in temp for item in sublist if
                 item.text.isalpha() is True and item.text[0].isupper() is True]
        return temp2

        return None

    def get_time_zone(self):

        if self.__country_card is None:
            self.scrap_document()

        time_zone_element = self.__country_card.find_all(text=re.compile("(UTC|GMT)"))[0].find_parent().find_parent()

        return time_zone_element.text

    def get_country_card(self):

        if self.__country_card is None:
            self.scrap_document()

        return self.__country_card
