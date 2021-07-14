from django.http.response import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
import json

from django.utils import timezone
from ...models import ShoppingList

def req(request, pk):
    body = request.body
    jsonBody = json.loads(body)
    shoppinglist = ShoppingList.objects.get(pk=pk)

    if 'name' in jsonBody:
        shoppinglist.name = jsonBody["name"]

    if 'display_name' in jsonBody:
        shoppinglist.display_name = jsonBody["display_name"]

    if 'owner' in jsonBody:
        user = User.objects.get(pk=jsonBody["owner"])
        shoppinglist.owner = user

    shoppinglist.last_change = timezone.now()
    shoppinglist.save()
    
    res = serializers.serialize("json", [shoppinglist])
    return HttpResponse(res, content_type="application/json")