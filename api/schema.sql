DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS languages;
DROP TABLE IF EXISTS political_regimes;
DROP TABLE IF EXISTS neighbours;
DROP TABLE IF EXISTS speaks;
DROP TABLE IF EXISTS implements;

CREATE TABLE countries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  capital TEXT UNIQUE NOT NULL,
  population INTEGER,
  area INTEGER
);

CREATE TABLE languages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE political_regimes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);


CREATE TABLE neighbours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_country_1 INTEGER REFERENCES countries(id),
    id_country_2 INTEGER REFERENCES countries(id)
);

CREATE TABLE speaks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_country INTEGER REFERENCES countries(id),
    id_language INTEGER REFERENCES languages(id)
);

CREATE TABLE implements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_country INTEGER REFERENCES countries(id),
    id_political_regimes INTEGER REFERENCES political_regimes(id)
);


