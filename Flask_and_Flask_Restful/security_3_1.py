# users = [
#   {
#     'id':1,
#     'username': 'shaan',
#     'password': 'memes'
#   }
# ]
#
# username_mapping = { 'shaan':  {
#     'id':1,
#     'username': 'shaan',
#     'password': 'memes'
#   }
# }
#
# userid_mapping = {1:{
#     'id':1,
#     'username': 'shaan',
#     'password': 'memes'
#   }
# }
# To crate above users and mapping we can define a User class and make
#things simpler

from werkzeug.security import safe_str_cmp
# to compare the string regardless of encoding used nad for different versions of python
from user3_2 import User

users = [
  User(1,"Shaan", "memes")
]
username_mapping = {user.username:user for user in users}
userid_mapping = {user.id:user for user in users}

def authenticate(username, password):
  user = username_mapping.get(username, None) # get the user "object"
  if user and safe_str_cmp(user.password, password):
    return user

def identity(payload): # this is uniques to Flask-JWT
  #payload is the content of JWT Token
  user_id = payload['identity']
  return userid_mapping.get(user_id, None)