import requests
import re


class DocumentGetter:
    """
    Clasa DocumentGetter are rolul de a face o cerere catre wikipedia pentru o resursa data.

    Expune metodele publica get_document, metoda ce face cererea catre server, folosindu-se de pachetul requests, si get_url, getter pentru campul `protected` care retine URL-ul resursei dorite.
    """

    _url = None

    def __init__(self, url):
        """
        Constructorul clasei DocumentGetter primeste ca parametru un string cu url-ul resursei ce se doreste a fi obtinuta. Intai, se verifica validitatea url-ului; daca acesta este un url valid catre pagina in limba engleza a Wikipediaeste initializat campul _url cu valoarea parametrului. In caz contrat este aruncata o exceptie.

        """

        validation_regex = re.compile("^https://en.wikipedia.org(.)*")

        if validation_regex.match(url):
            self._url = url
        else:
            raise Exception("Exception. Please enter a Wikipedia domain url.")

    def get_document(self):
        """
        Metoda face si trimite o cerere catre Wikipedia pt. un document dat si intoarce ca valoare de return continutul resursei, codificat utf-8.

        Parametrii: niciunul
        Valoare de retur: continutul, in format textual/utf-8, al raspunsului dat de wikipedia la cererea data.
        Efecte secundare: Network IO + Aruncarea unei exceptii in cazul in care campul _url este neinitializat.
        """

        if self._url is None:
            raise Exception("Exception. Please initialise the url first.")

        r = requests.get(self._url)
        return r.text

    def get_url(self):
        """
        Metoda reprezinta un getter pentru campul protected url. 

        Parametrii: Niciunul
        Valoare de retur: url-ul documentului Wikipedia.
        Efecte secundare: Aruncarea unei exceptii in cazul in care campul url este neinitializat.
        """

        if self._url is None:
            raise Exception("Exception. The url is uninitialised.")

        return self._url
