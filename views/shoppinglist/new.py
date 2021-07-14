from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.core import serializers
import json
from ...models import ShoppingList

def req(request):
    body = request.body
    jsonBody = json.loads(body)
    user = User.objects.get(pk=jsonBody["owner"])
    shoppinglist = ShoppingList.objects.create(
        name=jsonBody["name"],
        display_name=jsonBody["display_name"],
        owner=user
    )
    res = serializers.serialize("json", [shoppinglist])
    return HttpResponse(res, content_type="application/json")