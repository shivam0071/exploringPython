# REST are designed to be stateless....and be able to interact with resources

from flask import Flask , request, jsonify # To take a dictionary and coverts in into  a json (string)

app = Flask(__name__)

# END POINTS
# POST /store data : {name}
# GET /store/<string: name>
# GET /store
# POST /store/<string : name>/item {name:, price: }
# GET /store/<string : name>/item

# An actual Store
stores = [
  {
    "name" : "ThePokemonStop",
    "items" : [
      {
    'name': 'Pokeball',
    'price' : 10
      }
    ]
  }
]

@app.route("/")
def home():
  return "Hello"

@app.route("/store", methods = ['POST'])
def create_store():
  request_data = request.get_json() # the data coming from browser
  new_store = {"name":request_data["name"],
               "items":[]
              }
  stores.append(new_store)
  return jsonify(new_store)

@app.route("/store/<string:name>")  # localhost/store/name
def get_store(name):
  store = "Store Not Found"
  # import pdb
  # pdb.set_trace()
  for data in stores:
      if data["name"] == name:
        return jsonify(data)
  return jsonify({"message": store})

@app.route("/store")  # localhost/store
def get_stores():
  return jsonify({"stores": stores})

@app.route("/store/<string:name>/item", methods = ['POST'])  # localhost/store/name/item
def create_item_in_store(name):
  request_data = request.get_json()
  for data in stores:
      if data["name"] == name:
        data["items"].append(request_data)
        return jsonify(data)
  return jsonify({"message": "Store not found"})

@app.route("/store/<string:name>/item")  # localhost/store/name/item
def get_item_in_store(name):
  store = "Store Not Found"
  for data in stores:
      if data["name"] == name:
        return jsonify({"item": data["items"]})
  return jsonify({"message": store})


app.run()