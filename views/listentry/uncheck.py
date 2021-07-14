from django.http.response import HttpResponse
from django.core import serializers
from ...models import ListEntry

def uncheck(request, pk):
    listentry = ListEntry.objects.get(pk=pk)

    listentry.checked = False

    listentry.save()
    
    res = serializers.serialize("json", [listentry])
    return HttpResponse(res, content_type="application/json")