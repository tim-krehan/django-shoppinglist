import os, json
from typing import Text
from django.core import serializers
from django.core.files.storage import DefaultStorage
from django.http.response import HttpResponse

def req(request):
    storage = DefaultStorage()
    api_endpoint_files = storage.listdir(os.path.dirname(__file__))[1]
    api_endpoint_files.remove('__init__.py')
    api_endpoint_files.remove('urls.py')
    api_endpoint_files.remove('api.py')
    api_endpoints = [txt.replace('.py', '') for txt in api_endpoint_files]
    available_endpoints = {"available_endpoints": api_endpoints}
    jsonRes = json.dumps(available_endpoints)
    return HttpResponse(jsonRes, content_type="application/json")