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
    
    # Registering a blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    # However, the endpoint for the index view defined below will be blog.index. 
    # Some of the authentication views referred to a plain index endpoint. app.add_url_rule() 
    # associates the endpoint name 'index' with the / url so that url_for('index') or url_for('blog.index') 
    # will both work, generating the same / URL either way.

    # In another application you might give the blog blueprint a url_prefix and define a 
    # separate index view in the application factory, similar to the hello view. Then the index and 
    # blog.index endpoints and URLs would be different.
    return app