from django.core import serializers
from django.contrib.auth.models import User
from django.http.response import HttpResponse

def get(request, pk):
    usr = User.objects.filter(pk=pk)
    json = serializers.serialize("json", usr, fields=('username', 'first_name', 'last_name', 'email'))
    return HttpResponse(json, content_type="application/json")