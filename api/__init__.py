import os
from json import JSONDecoder
from flask import Flask, request
from api import db

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "api.sqlite"),
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
    db.init_app(app)

    @app.route("/hello")
    def hello():
        return "Hello, World!"


    @app.route("/get/<string:name>", methods=["GET"])
    def get_country(name):

        database = db.get_db()
        country = database.execute("SELECT * FROM countries WHERE name = ?", (name,)).fetchone()

        if country is None:
            abort(404, f"There is no country named {name}")

        return country

    @app.route("/post/country", methods=["POST"])
    def post_country():

        database = db.get_db()
        country = request.json
        print(country["name"])
        print(country["population"])
        print(country["area"])
        print(type(country))
        print("test")
        return country["name"]

    return app
