from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core import serializers

def new(request):
    res = serializers.deserialize("json", request.body)
    json = serializers.serialize("json", res)
    return HttpResponse(res, content_type="application/json")