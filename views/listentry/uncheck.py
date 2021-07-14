from django.http.response import HttpResponse
from django.core import serializers
from django.utils import timezone
from ...models import ListEntry

def req(request, pk):
    listentry = ListEntry.objects.get(pk=pk)

    listentry.checked = False
    listentry.save()
    listentry.shoppinglist.last_change = timezone.now()
    listentry.shoppinglist.save()
    
    res = serializers.serialize("json", [listentry])
    return HttpResponse(res, content_type="application/json")