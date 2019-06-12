from flask import Flask, jsonify, render_template, request
from flask_restful import reqparse, Resource, Api
from micro_service_actual_process import best_bands, best_pokemon, main

app = Flask(__name__)
api = Api(app)

class home_page(Resource):
  def get(self):
    return {"/best-bands" : "Returns the band names",
            "/best-pokemon": "Returns the best pokemon"}

class pokemon(Resource):
  def get(self):
    main()
    return {"Pokemon": best_pokemon()}

class bands(Resource):
  def get(self):
    main()
    return {"Pokemon": best_bands()}



# define the api paths
api.add_resource(home_page, "/")
api.add_resource(pokemon, "/best-pokemon")
api.add_resource(bands, "/best-bands")

if __name__ == "__main__":
  app.run(debug=True)