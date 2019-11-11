
import os
import json
from pip._internal import main

def install_pkg(package):
    main(['install', package])

try:
    import falcon
except ImportError:
    install_pkg('falcon')
try:
    import gunicorn
except ImportError:
    install_pkg('gunicorn')


from wsgiref import simple_server
import random
import time
from .resources import Things, RandomIntGen, DemoClass

if __name__ == '__main__':    
    app = falcon.API()
    app.add_route("/test", Things())
    app.add_route("/number", RandomIntGen())
    app.add_route("/demo", DemoClass())
    httpd = simple_server.make_server("localhost", 8000, app)
    print ("Serving on %s:%s" % (host, port))
    httpd.serve_forever() 
