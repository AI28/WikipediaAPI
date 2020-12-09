# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import re

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

    try:
        list_of_countries = ListOfCountriesScrapper("https://en.wikipedia.org/wiki/List_of_sovereign_states")
        wiki = "https://en.wikipedia.org"
        for j in list_of_countries.get_elements():

            aux = CountryDataScrapper(wiki + j)

            if aux.get_country_card() is None:
                continue

            country_name = aux.get_country_name()
            if country_name is None:
                continue

            country_area = aux.get_country_area()
            country_capital = aux.get_country_capital()
            country_population = aux.get_country_population()
            country_government = aux.get_country_government()
            country_language = aux.get_country_language()
            country_time_zone = aux.get_time_zone()
            country_population_density = None

            if country_population is None or country_area is None:
                country_population_density = 0

            country_population_density = country_population // country_area

            print(country_area)
            print(country_name)
            print(country_population)
            print(country_government)
            print(country_language)
            print(country_time_zone)
            print(country_population_density)

            t2 = {"name": country_name, "area": country_area, "population": country_population,
                  "government": country_government, "languages": country_language, "timezone": country_time_zone,
                  "density": country_population_density}

            print(json.dumps(t2))
            print(aux.get_neighbours())

    except Exception as e:
        print(str(e))
