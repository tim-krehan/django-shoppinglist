import sys
from django.core import serializers
from ...models import ListEntry
from django.http.response import HttpResponse

def list(request, pk):
    list = ListEntry.objects.filter(shoppinglist=pk)
    json = serializers.serialize("json", list)
    return HttpResponse(json, content_type="application/json")