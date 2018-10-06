# import http.server
# import socketserver
#
# PORT = 8000
#
# Handler = http.server.SimpleHTTPRequestHandler
#
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

import os
print(os.getcwd())

print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_dir = os.path.dirname(os.path.dirname(__file__))+'/HFPython/sketch.txt'
print (base_dir)
if os.path.isfile(base_dir):
  data = open(base_dir).read()
  print(data)
print(os.path.isfile('demo.txt'))