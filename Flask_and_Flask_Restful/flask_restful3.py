# 12:12
# 13/06/2019
from flask import  Flask, request
from flask_restful import Resource, Api
# Resource -  if api concerns with students then a resource is a student...a thing that API
# can return
from flask_jwt import JWT, jwt_required # To SETUP JWT # jwt_required to force the JWT on methods
from security_3_1 import authenticate, identity

app = Flask(__name__)
api = Api(app) # allows us to add the resources
app.secret_key = 'shaan_pokemon_trainer'
# we will use this for encryption
# this should be kept secret
jwt = JWT(app, authenticate, identity) # /auth
# JWT creates a new endpoint  /auth
# when we call /auth  we send it a username and a password
# the JWT take those username and pass to the authenticate function (just like oauth 2.0)
# so this /auth endpoint returns a JWT token that tells that the username and password are
# correct and this is indeed a genuine user
# now the Identity uses this JWT token to return the user information

# /auth returns the below token
# {                    headers(algo and token type HS256) + payload(user, pass) + (base64UrlEncode(header + payload) + secretkey)
#     "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjA0MjQ2NjYsImlhdCI6MTU2MDQyNDM2NiwibmJmIjoxNTYwNDI0MzY2LCJpZGVudGl0eSI6MX0.IQY-Wfuuy4aZFh7NFp77ChQpovISeF_JYE3KG_uXX5g"
# }

# An api works with resources and every resource must be a class

items = []

# /item/<name>
class Item(Resource):
  @jwt_required()
  # {
  #   "description": "Request does not contain an access token",
  #   "error": "Authorization Required",
  #   "status_code": 401
  # }
  #  OR the token gets expired
  #{
    # "description": "Signature has expired",
    # "error": "Invalid token",
    # "status_code": 401
  # }
  # To avoid this...include header line authorization as key and JTW full_token as value

  def get(self, name):
    data =  next(filter(lambda x: x["name"] == name, items), None) #next returns the first ites
    # if nothing is matched then return None
    return {"item":data}, 200 if data else 404

  def post(self, name):
    if next(filter(lambda x: x["name"] == name, items), None):
        return {"message":f"Item name {name} already exists"}, 400

    requested_data = request.get_json()
    # force means we do not need content-type in header...it will just look in the content and will
    # format it accordingly....# dont use it
    requested_data.update({"name":name})
    items.append(requested_data)
    return requested_data, 201
    # 201 = Created
    # 202 = accepted ... if creating an object takes time...we accept it

class Items(Resource):
  def get(self):
    if items:
      return {"ITEMS":items}, 200
    return {"message": "No items found"}, 404

api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items")
app.run(debug=True )