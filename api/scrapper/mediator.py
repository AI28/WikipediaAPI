import json
import os
from api.scrapper.document_scrapper import ListOfCountriesScrapper, CountryDataScrapper

def initialize_countries_map(list_of_countries):
    """
    Helper function used in the two functions bellow.
    Initialises an empty country dictionary, avoiding duplicates.
    """
    countries_map = {}

    for j in list_of_countries.get_elements():

        country_informal_name = j.split('/')[-1]

        if country_informal_name in countries_map:
            continue
        elif country_informal_name == "Zaire":
            continue

        countries_map[country_informal_name] = ""

    return countries_map


def get_country_by_name(name):
    """
    Generates a dictionary for and single country and serializes it.
    Used for testing purposes. May remove it.
    """
    wiki = "https://en.wikipedia.org/wiki/"

    aux = CountryDataScrapper(wiki + name)

    print(wiki + name)

    if aux.get_country_card() is None:
        return

    country_name = aux.get_country_name()
    if country_name is None:
        return

    country_area = aux.get_country_area()
    country_capital = aux.get_country_capital()
    country_population = aux.get_country_population()
    country_government = aux.get_country_government()
    country_language = aux.get_country_language()
    country_time_zone = aux.get_time_zone()
    country_population_density = None
    country_neighbours = None

    if country_population is None or country_area is None:
        country_population_density = 0
    else:
        country_population_density = country_population // country_area

    t2 = {"name": country_name, "capital": country_capital, "area": country_area, "population": country_population,
          "government": country_government, "languages": country_language, "timezone": country_time_zone,
          "density": country_population_density, "neighbours": country_neighbours}

    country_serialization = json.dumps(t2)
    print(country_serialization)

    if os.path.exists("serialized_countries") is False:
        os.mkdir("serialized_countries")
    open("serialized_countries/%s.json" % name, "wt").write(country_serialization)


def generate_countries_map():
    """
    Creates and populates a dictionary datastructure where the keys are the countries' names and the values are
    themselves dictionaries containing the countries' various characteristics. It also serialises each dictionary
    entry into a <key_name>.json file.
    """

    country_map = {}

    try:

        list_of_countries = ListOfCountriesScrapper("https://en.wikipedia.org/wiki/List_of_sovereign_states")
        wiki = "https://en.wikipedia.org"

        country_map = initialize_countries_map(list_of_countries)

        for j in list_of_countries.get_elements():

            country_informal_name = j.split('/')[-1]

            if country_map[country_informal_name] != "":
                continue
            elif country_informal_name == "Zaire":
                continue

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
            country_neighbours = list(set(filter(lambda x: x in country_map, aux.get_neighbours())))

            if country_population is None or country_area is None:
                country_population_density = 0
            else:
                country_population_density = country_population // country_area

            t2 = {"name": country_name, "capital": country_capital, "area": country_area, "population": country_population,
                  "government": country_government, "languages": country_language, "timezone": country_time_zone,
                  "density": country_population_density, "neighbours": country_neighbours}

            country_map[country_informal_name] = t2
            country_serialization = json.dumps(t2)
            if os.path.exists("serialized_countries") is False:
                os.mkdir("serialized_countries")
            open("serialized_countries/%s.json" % country_informal_name, "wt").write(country_serialization)


    except Exception as e:
        print(str(e))

    return country_map

