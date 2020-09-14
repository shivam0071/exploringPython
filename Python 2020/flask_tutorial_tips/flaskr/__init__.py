import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # instance_relative_config=True tells the app that configuration files are relative to the instance folder. 
    # The instance folder is located outside the flaskr package and can hold local data that shouldn’t be 
    # committed to version control, such as configuration secrets and the database file.

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # SECRET_KEY is used by Flask and extensions to keep data safe.
    # It’s set to 'dev' to provide a convenient value during development,
    # but it should be overridden with a random value when deploying.

    # DATABASE is the path where the SQLite database file will be saved. 
    # It’s under app.instance_path, which is the path that Flask has chosen for the instance folder.

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #  Flask doesn’t create the instance folder automatically, 
    # but it needs to be created because your project will create the SQLite database file there.

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # After creating db.py this is added
    from . import db
    db.init_app(app)
    # Now that init-db has been registered with the app, 
    # it can be called using the flask command, similar to the run command from the previous page.
    
    return app