from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core import serializers
import json

# POST
def req(request, pk):
    body = request.body
    jsonBody = json.loads(body)
    user = User.objects.get(pk=pk)
    if jsonBody['username'] != None :
        user.username = jsonBody["username"]

    if jsonBody['first_name'] != None :
        user.first_name = jsonBody["first_name"]

    if jsonBody['last_name'] != None :
        user.last_name = jsonBody["last_name"]

    if jsonBody['email'] != None :
        user.email = jsonBody["email"]

    if jsonBody['password'] != None :
        user.set_password(jsonBody["password"])

    user.save()
    
    res = serializers.serialize("json", [user], fields=('username', 'first_name', 'last_name', 'email'))
    return HttpResponse(res, content_type="application/json")