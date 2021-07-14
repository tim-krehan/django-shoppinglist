from django.http.response import HttpResponse
from django.core import serializers
import json
from ...models import ListEntry, Unit

def update(request, pk):
    body = request.body
    jsonBody = json.loads(body)
    listentry = ListEntry.objects.get(pk=pk)

    if jsonBody['amount'] != None :
        listentry.amount = jsonBody["amount"]

    if jsonBody['unit'] != None :
        unit = Unit.objects.get(pk=jsonBody["unit"])
        listentry.unit = unit

    if jsonBody['name'] != None :
        listentry.name = jsonBody["name"]

    listentry.save()
    
    res = serializers.serialize("json", [listentry])
    return HttpResponse(res, content_type="application/json")