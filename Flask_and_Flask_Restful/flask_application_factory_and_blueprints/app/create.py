import urllib3
from importlib import import_module
from logging import config as logging_config
from typing import Union # ??

from flask import Flask
from app.blueprints import blueprints  # the blueprints
from app.extensions import init_extensions # init the swagger, mail etc

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_app(config: Union[str, None] = None, path: str = "config") -> Flask:
    app = Flask(__name__)
    
    # app.config.from_object(import_module(path).Prod)

    # if config:
        # app.config.dict_config(obj=f"{path}.{config}")

    # logging_config.dictConfig(app.config["LOG_CONF"])   # FROM config file

    init_extensions(app)

    for bluep in blueprints:
        import_module(bluep.import_name)    # import the view - 'app.views.corona'
        app.register_blueprint(bluep)
        
    return app