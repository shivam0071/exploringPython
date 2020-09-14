from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_caching import Cache     #Exploring Cache..not working

cors = CORS()
mail = Mail()
swagger = Swagger()
cache = Cache(config={'CACHE_TYPE':'simple'})

def init_extensions(app: Flask):
    cors.init_app(app)
    mail.init_app(app)
    swagger.init_app(app)
    cache.init_app(app)