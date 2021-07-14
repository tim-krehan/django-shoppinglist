import os, json
from django.core import serializers
from django.core.files.storage import DefaultStorage
from django.http.response import HttpResponse

def req(request):
    storage = DefaultStorage()
    api_endpoints = storage.listdir(os.path.dirname(__file__))[0]
    api_endpoints.remove('__pycache__')
    available_endpoints = {"available_endpoints": api_endpoints}
    jsonRes = json.dumps(available_endpoints)
    return HttpResponse(jsonRes, content_type="application/json")