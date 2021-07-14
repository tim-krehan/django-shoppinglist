from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core import serializers
import json

def req(request):
    body = request.body
    jsonBody = json.loads(body)
    user = User.objects.create_user(
        jsonBody["username"],
        jsonBody["email"],
        password=jsonBody["password"],
        first_name=jsonBody["first_name"],
        last_name=jsonBody["last_name"]
    )
    res = serializers.serialize("json", [user], fields=('username', 'first_name', 'last_name', 'email'))
    return HttpResponse(res, content_type="application/json")