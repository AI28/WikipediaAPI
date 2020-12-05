# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Scraper.DocumentScrapper import ListOfCountriesScrapper, CountryDataScrapper


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    test1 = None

    try:
        test1 = ListOfCountriesScrapper("https://en.wikipedia.org/wiki/List_of_sovereign_states")
    except Exception as e:
        print(str(e))
        return

    return test1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    docs = print_hi()
    docs.scrap_document()
    test = docs.get_elements()

    test = []
    try:
        wiki = "https://en.wikipedia.org"
        for i in docs.get_elements():


            aux = CountryDataScrapper(wiki + i)

            if aux.get_country_card() is None:
                continue

            test.append(aux)
            for j in aux.get_country_card().children:
                print(j)


    except Exception as e:
        print(str(e))


