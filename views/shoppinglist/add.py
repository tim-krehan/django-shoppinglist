from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.core import serializers
import json

from django.utils import timezone
from ...models import ShoppingList, ListEntry, Unit

def req(request, pk):
    body = request.body
    jsonBody = json.loads(body)

    shoppinglist = ShoppingList.objects.get(pk=pk)
    unit = Unit.objects.get(pk=jsonBody["unit"])
    user = User.objects.get(pk=14)
    listentry = ListEntry.objects.create(
        shoppinglist=shoppinglist,
        amount=jsonBody["amount"],
        unit=unit,
        name=jsonBody["name"],
        added_by=user
    )
    shoppinglist.last_change = timezone.now()
    shoppinglist.save()
    
    res = serializers.serialize("json", [listentry])
    return HttpResponse(res, content_type="application/json")