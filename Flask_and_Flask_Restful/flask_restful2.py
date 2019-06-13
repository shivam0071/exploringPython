# 12:12
# 13/06/2019
from flask import  Flask
from flask_restful import Resource, Api
# Resource -  if api concerns with students then a resource is a student...a thing that API
# can return


app = Flask(__name__)
api = Api(app) # allows us to add the resources

# An api works with resources and every resource must be a class

class Student(Resource): # http://127.0.0.1:5000/student/Shivam
  def get(self, name):
    return {'student': name}

api.add_resource(Student, "/student/<string:name>") #localhost/student/shaan

app.run()