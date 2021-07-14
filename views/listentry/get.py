import sys
from django.core import serializers
from ...models import ListEntry
from django.http.response import HttpResponse

def get(request, pk):
    entry = ListEntry.objects.get(pk=pk)
    json = serializers.serialize("json", [entry])
    return HttpResponse(json, content_type="application/json")