# -*- coding: utf-8 -*-
"""
Unittests and mock tests
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
from falcon.main import api
from falcon.resources import Things, RandomIntGen, DemoClass
try:
    import pytest
except ImportError:
    install_pkg('pytest')
from falcon import testing

@pytest.fixture
def client():
    testing.TestClient(api)
def test_addition_Things(client):
    body = [{"id": 1, "name": "TestClient"},{"id": 2, "name": "JsonTest"}]
    response = client.simulate_get(path='/test', method='GET')
    assert response.status = falcon.HTTP_200
    assert response.headers['SampleHeader'] == 'True'
    assert response.body == body
    


    
    
    
    