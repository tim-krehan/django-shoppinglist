from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core import serializers
import json

# POST
def req(request, pk):
    body = request.body
    jsonBody = json.loads(body)
    user = User.objects.get(pk=pk)
    if 'username' in jsonBody:
        user.username = jsonBody["username"]

    if 'first_name' in jsonBody:
        user.first_name = jsonBody["first_name"]

    if 'last_name' in jsonBody:
        user.last_name = jsonBody["last_name"]

    if 'email' in jsonBody:
        user.email = jsonBody["email"]

    if 'password' in jsonBody:
        user.set_password(jsonBody["password"])

    user.save()
    
    res = serializers.serialize("json", [user], fields=('username', 'first_name', 'last_name', 'email'))
    return HttpResponse(res, content_type="application/json")