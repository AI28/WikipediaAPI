import os
from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from api import db

    db.init_app(app)
    mongo = db.get_db(app)

    @app.route("/top10/<field>")
    def top10(field):
        wikipedia = mongo.db["wikipedia"]
        countries = wikipedia["countries"]
        doc_result = countries.find({}, {"_id": 0, "name": 1, field: 1}).sort(field, -1).limit(10)
        return (list(doc_result)).__str__()

    @app.route("/get-by/language/<language>")
    def get_by_language(language):
        wikipedia = mongo.db["wikipedia"]
        countries = wikipedia["countries"]
        doc_result = countries.find({"languages":language}, {"_id": 0, "name": 1})
        return (list(doc_result)).__str__()

    @app.route("/get-by/regime/<regime>")
    def get_by_regime(regime):
        wikipedia = mongo.db["wikipedia"]
        countries = wikipedia["countries"]
        doc_result = countries.find({"government":regime}, {"_id": 0, "name": 1})
        return (list(doc_result)).__str__()

    @app.route("/get-by/timezone/<timezone>")
    def get_by_timezone(timezone):
        wikipedia = mongo.db["wikipedia"]
        countries = wikipedia["countries"]
        doc_result = countries.find({"timezone": timezone}, {"_id": 0, "name": 1})
        return (list(doc_result)).__str__()

    @app.route("/get/<name>")
    def get_by_name(name):

        wikipedia = mongo.db["wikipedia"]
        countries = wikipedia["countries"]
        doc_result = countries.find_one({"name": name}, {"_id": 0, "name": 1, "languages": 1})
        return (list(doc_result)).__str__()

    return app
