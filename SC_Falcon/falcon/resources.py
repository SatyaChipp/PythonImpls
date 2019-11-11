# -*- coding: utf-8 -*-
"""
Resources for Falcon REST APIs
GET, PUT, POST, DELETE,HEAD
"""
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

class Things:
    def on_get(self, req, res):
        res.body = json.dumps([{"id": 1, "name": "TestClient"}, 
                               {"id": 2, "name": "JsonTest"}])
        res.status = falcon.HTTP_200
        res.set_header('SampleHeader', 'True')



class RandomIntGen:
    genWaitTime = int(os.environ.get('WAIT_TIME', '1.5'))
    def on_get(self, req, res):
        time.sleep(genWaitTime) #wait time between numbers
        number = random.randint(0, 1000)
        result = {'start': 0, 'end': 1000, 'number': number}
        res.media = result
        res.status = falcon.HTTP_200

class DemoClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

        data = json.dumps({"Name": "Lulu", "Title": "Lead Architect"})
        print("Demo Success for GET")

        output = {
            'msg' : 'Hello {0} ! Welcome to Saturn Cloud Falcon Challenge'.format(data['Name'])
        }
        resp.body = json.dumps(output)

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
    
        data = json.loads(req.stream.read())
    
        sum_ = int(data['x']) + int(data['y'])
    
        output = {
            'msg' : 'x: {0} + y: {1} = {2}'.format(data['x'],data['y'],sum_)
        }
        resp.body = json.dumps(output)
    
    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200
        output = {
            'msg' : 'Updates not supported'
        }
    
        resp.body = json.dumps(output)
    
    def on_delete(self, req, resp):
        resp.status = falcon.HTTP_200
        output = {
            'msg' : 'Delete not supported '
        }
    
        resp.body = json.dumps(output)
