import os.path
import click
import json
from flask.cli import with_appcontext
from flask.cli import current_app
from flask_pymongo import PyMongo
from flask import g
import api.scrapper.mediator


def init_db(app, put_values=False):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/wikipedia"
    mongo = PyMongo(app)

    if put_values:
        init_with_values()

    return mongo


def get_db(app):
    with app.app_context():
        if 'db' not in g:
            g.db = init_db(app)

        return g.db


def init_with_values():
    wikipedia = get_db().db["wikipedia"]
    countries = wikipedia["countries"]

    for (root, directories, files) in os.walk("serialized_countries"):
        for fileName in files:
            file_content = open((os.path.join(root, fileName)), "r").read()
            countries.insert_one(json.loads(file_content))


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_with_values(current_app, True)
    click.echo("Initialized the database.")


@click.command("scrape")
@with_appcontext
def scrap_wiki():
    """
    Begin data mining process.
    """
    api.scrapper.mediator.generate_countries_map()


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.cli.add_command(init_db_command)
    app.cli.add_command(scrap_wiki)
