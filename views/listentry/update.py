from django.http.response import HttpResponse
from django.core import serializers
import json

from django.utils import timezone
from ...models import ListEntry, Unit

def req(request, pk):
    body = request.body
    jsonBody = json.loads(body)
    listentry = ListEntry.objects.get(pk=pk)

    if 'amount' in jsonBody:
        listentry.amount = jsonBody["amount"]

    if 'unit' in jsonBody:
        unit = Unit.objects.get(pk=jsonBody["unit"])
        listentry.unit = unit

    if 'name' in jsonBody:
        listentry.name = jsonBody["name"]

    listentry.save()
    listentry.shoppinglist.last_change = timezone.now()
    listentry.shoppinglist.save()
    
    res = serializers.serialize("json", [listentry])
    return HttpResponse(res, content_type="application/json")